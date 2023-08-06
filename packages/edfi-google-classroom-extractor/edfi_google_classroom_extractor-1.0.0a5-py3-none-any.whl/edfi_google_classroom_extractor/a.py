# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

import logging
import sys

from edfi_google_classroom_extractor import facade
from edfi_google_classroom_extractor.helpers.arg_parser import MainArguments


logging.basicConfig(
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        level="INFO",
    )

arguments = MainArguments(
    "admin@ibamonitoring.org",
    "INFO",
    "gc_data",
    "2020-08-01",
    "2021-05-31"
)

facade.run(arguments)

