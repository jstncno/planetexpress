# First, update and upgrate
apt-get update
apt-get upgrade

# Install NFS tools
apt-get install nfs-kernel-server portmap nfs-common

# Install exFAT tools
apt-get install exfat-fuse exfat-utils
