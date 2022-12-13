"""
This module contains the backends implementing the supported OpenVPN protocols.
"""
from .openvpn import OpenVPNTCP, OpenVPNUDP

__all__ = ["OpenVPNTCP", "OpenVPNUDP"]
