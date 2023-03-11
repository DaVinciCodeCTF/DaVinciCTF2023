#!/bin/env sh

resource=`pwgen 8 1`

echo hashcash -mb28 $resource

read result

hashcash -cdb28 -r $resource "$result"   &&
    qemu-system-x86_64 -kernel bzImage     \
    -initrd initramfs.cpio.gz -nographic \
    -append "console=ttyS0"

