#!/usr/bin/env python3
# Copyright 2020 Enapter, Alexander Shalin <ashalin@enapter.com>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distribut$
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express o$
# See the License for the specific language governing permissions and limitatio$

import sys
import struct
from pymodbus.client.sync import ModbusTcpClient

ip = sys.argv[1]
port = 502
register = 4 # Reboot. 1 = Reboot.
value = 1

device = ModbusTcpClient(ip, port)
print(device.write_register(register, value, unit=1))
