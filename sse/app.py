from sseclient import SSEClient
from keen.client import KeenClient
import json

client = KeenClient(
    project_id="50ba759d897a2c45c2000000",
    write_key="72a1ad85456fd2361cfe8b65d240eab16b083caa944c11d9507761e536d34822eca4cefad12e482373ee41278953f98c6ff724b33b56fd5971e8d34cdd284cb6c3f202d9f13329e39c01eb9a35d1124cae81d9a4505992fce03be4030e32b19c72df266c55a18937f001e7158f6eac44",
    read_key="f7a829ecc9e237949b0b97245c828661ff0c9f46eaec35a7dc4cfd3b4ef42804f5fc1859ecad05bd7d72b6c3a2e4047ae39cba86b5d51c770be26b0a406cbb44650d20fd05fb7896293f015cec3af3ca2df8a507927bf4cfed9275eb89e8dee855cf45db75b221074bda2f737d2810f2"
)

headers = {"Accept": "text/event-stream"}

messages = SSEClient('https://flickering-fire-322.firebaseio.com/.json', headers=headers)

first = True

for msg in messages:
    print msg.event
    print msg.data
    if not first and 'put' in msg.event:
        data = json.loads(msg.data)
        path = data['path'].split("/")
        device = path[1]
        timestamp = path[2]
        data = int(data['data'])
        event = {
            "device": device,
            "volume": data,
            "timestamp": timestamp
        }
        client.add_event("flow", event)
    first = False
