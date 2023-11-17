from .connection import select_port, AuraConnectionError, node_id_to_int
from .auraclient import AuraClient
from .aurahub import AuraHub
from typing import Union


def select_client(port_hint: Union[str, int] = None,
                  device_hint: Union[str, int] = None,
                  verbose: bool = False):

    port_name = select_port(port_hint=port_hint)

    if not port_name:
        if port_hint:
            raise AuraConnectionError(f'invalid port choice: {port_hint}')
        else:
            raise AuraConnectionError(f"No serial ports found - make sure Aura is connected to your computer")

    aura_hub = AuraHub(port_name)

    if device_hint == 'gw':
        return aura_hub

    with aura_hub:

        if aura_hub.has_direct_aura_mc_connection():
            return AuraClient(port_name=port_name, aura_hub=aura_hub)
        else:
            aura_hub_name = aura_hub.pull_name()
            aura_hub_id = aura_hub.pull_can_id()

            if verbose:
                print(f"Connected to Aura gateway {aura_hub_name} on {aura_hub.get_port_name()}")

            device_hint_int = None
            if device_hint is not None:
                try:
                    device_hint_int = int(device_hint)
                    if aura_hub_id == device_hint_int:
                        return aura_hub
                except ValueError:
                    pass

                if device_hint == aura_hub_name:
                    return aura_hub

            scanned_nodes = aura_hub.scan_aura_can(with_name=True)

            if len(scanned_nodes) == 0:
                if verbose:
                    print("The gateway did not find any Aura actuator")

                if device_hint is not None:
                    raise AuraConnectionError(f'No device found for id {device_hint}')

                return aura_hub

            else:
                nodes_by_id = dict((node_id_to_int(node_info.id), node_info) for node_info in scanned_nodes)
                selected_id = None

                if device_hint is not None:
                    for node_id, node_info in nodes_by_id.items():
                        if node_info.name == device_hint or node_id == device_hint_int:
                            selected_id = node_id
                            break
                    else:
                        msg = f'No device found for id {device_hint}'
                        #msg += f" ({', '.join(str(node_id) for node_id in nodes_by_id)} are available)"
                        raise AuraConnectionError(msg)

                else:

                    print("Available devices:")
                    while True:
                        print(f'[gw] {aura_hub_id}: {aura_hub.pull_name()}')
                        for node_id, node_info in nodes_by_id.items():
                            print(f'     {node_id}: {node_info.name}')

                        selected_id = list(nodes_by_id.keys())[0]
                        user_input = input(f'select device: [default: {selected_id}]\n')
                        if user_input:
                            if user_input in ('g', 'gw'):
                                return aura_hub
                            try:
                                selected_id = int(user_input)
                                if selected_id == aura_hub_id:
                                    return aura_hub
                                if selected_id in nodes_by_id:
                                    break
                            except ValueError:
                                pass
                                print('invalid selection:', selected_id)
                                print()
                        else:
                            break  # use selection default

                return AuraClient(port_name=port_name,
                                  aura_hub=aura_hub,
                                  aura_id=nodes_by_id[selected_id].id)
