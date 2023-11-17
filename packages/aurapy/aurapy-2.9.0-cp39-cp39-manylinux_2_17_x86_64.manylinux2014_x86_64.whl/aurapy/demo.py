from .auraclient import AuraClient
import time
import asyncio
from . import timer


def start_stop(dutycycle=0.15,
               run_for_secs=10):
    """
    Spins the motor in speed mode.
    :param dutycycle: desired pwm dutycycle in [-1, 1]
    :param run_for_secs: number of seconds to spin for
    """
    with AuraClient() as c:

        c.command_dutycycle(dutycycle)

        for i in range(run_for_secs):
            print(f"speed is {c.pull_state().speed:.0f}")
            time.sleep(1)

        c.stop()


async def _alternate_directions_loop(aura_client,
                                     dutycycle=0.2,
                                     run_for_secs=10,
                                     toggle_direction_secs=3,
                                     do_sample=False):
    """
    Spins the motor alternatively in the two directions.
    :param aura_client: a connected aura client instance
    :param dutycycle: desired pwm dutycycle in [-1, 1]
    :param run_for_secs: number of seconds to run for
    :param toggle_direction_secs: time before reversing direction
    """

    time_start = time.time()
    time_end = time_start + run_for_secs

    time_switch_end = time_start
    i = 0
    while time.time() < time_end:
        if do_sample:
            state = aura_client.pull_state()
            print(f"{i} speed is {state.speed:5.0f}; temperature: {state.board_temp:3.2f}")

        i += 1
        await asyncio.sleep(1)

        if time.time() > time_switch_end:
            time_switch_end = time.time() + toggle_direction_secs
            dutycycle *= -1
            aura_client.command_dutycycle(dutycycle)

    aura_client.stop()


def alternate_directions(dutycycle=0.2,
                         run_for_secs=10,
                         toggle_direction_secs=3):
    """
    Spins the motor alternatively in the two directions.
    :param dutycycle: desired pwm dutycycle in [-1, 1]
    :param run_for_secs: number of seconds to run for
    :param toggle_direction_secs: time before reversing direction
    """
    with AuraClient() as c:
        asyncio.run(
            _alternate_directions_loop(c,
                                       dutycycle,
                                       run_for_secs,
                                       toggle_direction_secs,
                                       do_sample=True))


async def _sample_speed_loop(aura_client,
                             sample_time_sec,
                             sample_freq_hz,
                             time_calls=False):
    """
    Gather speed measurements at regular intervals.
    Time how long it takes.

    :param sample_time_sec: sample time in seconds
    :param sample_freq_hz: sampling frequency in hertz
    :return: speed samples
    """

    if time_calls:
        pull_state = timer.Timer()(aura_client.pull_state)
    else:
        pull_state = aura_client.pull_state

    num_samples = int(sample_time_sec * sample_freq_hz)
    speed_samples = [0] * num_samples
    for i in range(num_samples):
        speed_samples[i] = pull_state().speed
        await asyncio.sleep(1/sample_freq_hz)

    #c._aura_client_impl.print_rx_tx_stats()

    return speed_samples


def sample_speed(sample_time_sec=5,
                 sample_freq_hz=100):
    """
    Gather speed measurements at regular intervals.
    Time how long it takes.

    :param sample_time_sec: sample time in seconds
    :param sample_freq_hz: sampling frequency in hertz
    """
    with AuraClient() as c:
        return asyncio.run(
            _sample_speed_loop(c,
                               sample_time_sec,
                               sample_freq_hz,
                               time_calls=True))


def collect_phase_samples(num_samples=100, step=1):

    with AuraClient() as c:
        with timer.Timer() as t:
            future = c.collect_phase_samples(num_samples, step)
            samples = future.get()

        num_samples_received = len(samples)
        print(f'collected {num_samples_received} samples in {t.elapsed_time():.2f}s, '
              f'so about {num_samples_received/t.elapsed_time()/1000:.2f}kHz')
        print()
        print(f'here are the first 3 samples:')
        for sample in samples[:3]:
            print(str(sample))

        print(''.join(c._aura_client_impl.send_ascii_command('tim', 1)))
        print(''.join(c._aura_client_impl.send_ascii_command('comm', 1)))
    return samples


async def _async_measurements(run_for_secs=5,
                              sample_freq_hz=10):

    with AuraClient() as c:

        task1 = _alternate_directions_loop(
            c,
            dutycycle=0.3,
            run_for_secs=run_for_secs)

        task2 = _sample_speed_loop(
            c,
            sample_time_sec=run_for_secs,
            sample_freq_hz=sample_freq_hz)

        _, speed_samples = await asyncio.gather(task1, task2)

        return speed_samples


def async_measurements(run_for_secs=5, sample_freq_hz=10):
    """
    asynchronous regime change and speed measurement:
        sample speed at the same time as commands are being sent.
    :param run_for_secs:
    :param sample_freq_hz:
    :return: speed samples
    """
    return asyncio.run(_async_measurements(run_for_secs=run_for_secs,
                                           sample_freq_hz=sample_freq_hz))


def ramp(num_cycles=10, ramp_duration_sec=10, min_duty=0.08, max_duty=0.18):
    """ duty cycle ramp """
    sleep_time = 0.3

    DEBUG = False

    range1 = int(ramp_duration_sec / sleep_time)

    cycles_counter = 0

    with AuraClient() as mot1:
        while cycles_counter < num_cycles:
            try:
                cycles_counter += 1
                # accelerate
                delta_duty = (max_duty - min_duty) / (ramp_duration_sec / sleep_time)

                for i in range(range1):
                    cmd = min_duty + i * delta_duty
                    if cmd > max_duty:
                        cmd = max_duty
                    mot1.command_dutycycle(cmd)
                    if DEBUG:
                        print(f"accel {cmd:.3f}")
                    time.sleep(sleep_time)

                # decelerate
                print(f"deceleration {cycles_counter}")
                #delta_duty = max_duty / (ramp_duration_sec / sleep_time)

                for i in range(range1):
                    cmd = max_duty - (i * delta_duty)
                    if cmd > max_duty:
                        cmd = max_duty

                    mot1.command_dutycycle(cmd)
                    if DEBUG:
                        print(f"decel {cmd:.3f}")
                    time.sleep(sleep_time)

            except KeyboardInterrupt:
                break
            except Exception as exc:
                print(exc)
