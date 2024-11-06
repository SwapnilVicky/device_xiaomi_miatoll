#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024-2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

module = ExtractUtilsModule(
    'miatoll',
    'xiaomi',
    check_elf=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'sm6250-common', module.vendor)
    utils.run()
