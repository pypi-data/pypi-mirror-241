from ._aura_pybind import AuraMCSim, AuraModel, aura_mc_conf_t
from datetime import timedelta
from aurapy.units import milliohms, celsius, rpm, milliseconds, dutycycles


def example_1():
    print()

    # create an instance of a simulated Aura device
    sim_instance = AuraMCSim("example1", AuraModel.AURA_M_450)

    # set real_time False for faster simulation
    sim_instance.set_track_real_time(False)
    print(sim_instance)

    print("The following hardware params can be edited before the simulation runs:")
    print(sim_instance.initial_sim_state.hardware)
    sim_instance.initial_sim_state.hardware.res = milliohms(500)

    print("real time elapsed:", sim_instance.real_time())
    print(" sim time elapsed:", sim_instance.simulated_time())
    # Finalize initialization so the sim device goes in a state where it can accept inputs
    sim_instance.run_until_init_done()

    # Turn off heartbeat checks (not needed for simulation)
    config = sim_instance.get_configuration()
    config.heartbeat_timeout = milliseconds(10000)
    sim_instance.set_configuration(config, True)

    print()
    print("the following environment inputs can be tweaked during the simulation:")
    print(sim_instance.env_inputs)

    # this sets the ambient temperature:
    sim_instance.env_inputs.ambient_temp = celsius(70)

    print("real time elapsed:", sim_instance.real_time())
    print(" sim time elapsed:", sim_instance.simulated_time())

    # set 20% dutycycle
    sim_instance.set_dutycycle(dutycycles(0.2))
    print("is_paused", sim_instance.is_paused())
    # request sampling of 1000 samples
    sim_instance.set_sampling(1000)
    print("Let the simulation run for some time")
    sim_instance.run_for_time(timedelta(seconds=0.2))
    print()
    print("real time elapsed:", sim_instance.real_time())
    print(" sim time elapsed:", sim_instance.simulated_time())
    print()
    print(sim_instance.get_latest_state())
    print()
    print(f"{len(sim_instance.sampled_currents)} sampled currents:")
    for currents in sim_instance.sampled_currents[-10:]:
        print(currents)


if __name__ == "__main__":
    example_1()
