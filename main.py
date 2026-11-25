import os
from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI

load_dotenv(override=True)

proxmox = ProxmoxAPI(
    os.getenv("PVE_HOST"),
    user=os.getenv("PVE_USER"),
    token_name=os.getenv("PVE_TOKEN_NAME"),
    token_value=os.getenv("PVE_TOKEN_VALUE"),
    verify_ssl=False,
)

resources = proxmox.cluster.resources.get()

nodes = [r for r in resources if r["type"] == "node"]
guests = [r for r in resources if r["type"] == ("qemu", "lxc")]