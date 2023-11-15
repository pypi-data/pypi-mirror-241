import struct
import sensirion_driver_adapters.mocks.response_provider as rp


class Svm4xResponseProvider(rp.ResponseProvider):

    RESPONSE_MAP = {0xd0: {0: struct.pack('>32s', rp.random_ascii_string(32)),
                           1: struct.pack('>8s', rp.random_ascii_string(8)),
                           3: struct.pack('>32s', rp.random_ascii_string(32))}
                    }

    def get_id(self) -> str:
        return 'Svm4xResponseProvider'

    def handle_command(self, cmd_id: int, data: bytes, response_length: int) -> bytes:
        sub_cmd_map = self.RESPONSE_MAP.get(cmd_id, None)
        if sub_cmd_map is None:
            return rp.random_bytes(response_length)
        if None in sub_cmd_map:
            return sub_cmd_map[None]
        assert len(data) >= 1, "No subcommand specified!"
        actual_subcommand = data[0]
        return sub_cmd_map.get(actual_subcommand, rp.random_bytes(response_length))
