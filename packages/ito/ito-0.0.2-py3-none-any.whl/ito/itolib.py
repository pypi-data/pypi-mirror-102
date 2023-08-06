# BSD 3-Clause License
#
# Copyright (c) 2004-2021 The ito developers.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

########################################################################################################################

import ctypes as ct
import os
import platform

########################################################################################################################


def load_library_path():
    os_platform_name = platform.uname()[0]
    if os_platform_name == "Linux":
        library_binary_file = "libitosdk.so"
    elif os_platform_name == "Windows":
        library_binary_file = "itosdk.dll"
    else:
        raise ValueError("Unsupported platform " + os_platform_name)

    library_directory = os.path.dirname(__file__)

    return os.path.join(library_directory, library_binary_file)


ito_dll = ct.CDLL(load_library_path())

########################################################################################################################

__encoding__ = "utf-8"

########################################################################################################################
ito_dimensions_func = ito_dll.ito_dimensions
ito_dimensions_func.arg_types = [ct.c_char_p, ct.c_ulong,
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.c_ulong,
                                 ct.c_ulong,
                                 ct.POINTER(ct.c_ubyte), ct.c_ulong,
                                 ct.c_char_p, ct.c_ulong]
########################################################################################################################
ito_properties_func = ito_dll.ito_properties
ito_properties_func.arg_types = [ct.c_char_p, ct.c_ulong,
                                 ct.POINTER(ct.c_char),
                                 ct.POINTER(ct.c_char),
                                 ct.POINTER(ct.c_char),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_bool),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.POINTER(ct.c_ulong),
                                 ct.c_ulong,
                                 ct.c_ulong,
                                 ct.POINTER(ct.c_ubyte), ct.c_ulong,
                                 ct.c_char_p, ct.c_ulong]
########################################################################################################################
ito_payments_func = ito_dll.ito_payments
ito_payments_func.arg_types = [ct.c_char_p, ct.c_ulong,
                               ct.c_ulong,
                               ct.POINTER(ct.c_double),
                               ct.POINTER(ct.c_double),
                               ct.c_ulong,
                               ct.c_ulong,
                               ct.POINTER(ct.c_ubyte), ct.c_ulong,
                               ct.c_char_p, ct.c_ulong]
########################################################################################################################
ito_payments_with_gradients_func = ito_dll.ito_paymentsWithGradients
ito_payments_with_gradients_func.arg_types = [ct.c_char_p, ct.c_ulong,
                                              ct.c_ulong,
                                              ct.POINTER(ct.c_double),
                                              ct.POINTER(ct.c_double),
                                              ct.POINTER(ct.c_double),
                                              ct.POINTER(ct.c_double),
                                              ct.c_ulong,
                                              ct.c_ulong,
                                              ct.POINTER(ct.c_ubyte), ct.c_ulong,
                                              ct.c_char_p, ct.c_ulong]
########################################################################################################################
ito_error_num_errors_func = ito_dll.ito_errorNumErrors
ito_error_num_errors_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                       ct.POINTER(ct.c_ulong),
                                       ct.POINTER(ct.c_ulong),
                                       ct.POINTER(ct.c_ulong)]
########################################################################################################################
ito_error_code_func = ito_dll.ito_errorCode
ito_error_code_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                 ct.c_ulong,
                                 ct.POINTER(ct.c_int)]
########################################################################################################################
ito_error_path_func = ito_dll.ito_errorPath
ito_error_path_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                 ct.c_ulong,
                                 ct.POINTER(ct.c_ulong)]
########################################################################################################################
ito_error_message_size_func = ito_dll.ito_errorMessageSize
ito_error_message_size_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                         ct.c_ulong,
                                         ct.POINTER(ct.c_ulong)]
########################################################################################################################
ito_error_message_func = ito_dll.ito_errorMessage
ito_error_message_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                    ct.c_ulong,
                                    ct.c_char_p]
########################################################################################################################
ito_error_num_positions_func = ito_dll.ito_errorNumPositions
ito_error_num_positions_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                          ct.c_ulong,
                                          ct.POINTER(ct.c_ulong)]
########################################################################################################################
ito_error_first_position_func = ito_dll.ito_errorFirstPosition
ito_error_first_position_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                           ct.c_ulong,
                                           ct.c_ulong,
                                           ct.POINTER(ct.c_ulong)]
########################################################################################################################
ito_error_first_line_func = ito_dll.ito_errorFirstLine
ito_error_first_line_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                       ct.c_ulong,
                                       ct.c_ulong,
                                       ct.POINTER(ct.c_ulong)]
########################################################################################################################
ito_error_first_offset_func = ito_dll.ito_errorFirstOffset
ito_error_first_offset_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                         ct.c_ulong,
                                         ct.c_ulong,
                                         ct.POINTER(ct.c_ulong)]
########################################################################################################################
ito_error_last_position_func = ito_dll.ito_errorLastPosition
ito_error_last_position_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                          ct.c_ulong,
                                          ct.c_ulong,
                                          ct.POINTER(ct.c_ulong)]
########################################################################################################################
ito_error_last_line_func = ito_dll.ito_errorLastLine
ito_error_last_line_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                      ct.c_ulong,
                                      ct.c_ulong,
                                      ct.POINTER(ct.c_ulong)]
########################################################################################################################
ito_error_last_offset_func = ito_dll.ito_errorLastOffset
ito_error_last_offset_func.arg_types = [ct.POINTER(ct.c_ubyte),
                                        ct.c_ulong,
                                        ct.c_ulong,
                                        ct.POINTER(ct.c_ulong)]


########################################################################################################################

def make_bytes_buffer(size):
    # if size is zero then ct.create_string_buffer raises "byte string too long"
    if size == 0:
        size = 1
    return ct.create_string_buffer(b'\000', size)


def make_chars_buffer(size):
    # if size is zero then ct.create_string_buffer raises "byte string too long"
    if size == 0:
        size = 1
    return ct.create_string_buffer(b'\000', size)


def make_bools_buffer(size):
    return (ct.c_bool * size)(*([False] * size))


def make_ints_buffer(size):
    return (ct.c_ulong * size)(*([0] * size))


def make_floats_buffer(size):
    return (ct.c_double * size)(*([0.0] * size))


def extract(lst, step):
    ret = []
    for i in range(0, len(lst), step):
        ret.append(lst[i:i + step].decode(__encoding__).rstrip('\000'))
    return ret


def ito_dimensions(definition,
                   max_executions, memory_foot_print,
                   error_buffer_size,
                   token):
    num_dates = ct.c_ulong()
    max_date_properties_size = ct.c_ulong()
    num_currencies = ct.c_ulong()
    max_currency_properties_size = ct.c_ulong()
    num_keys = ct.c_ulong()
    max_key_properties_size = ct.c_ulong()
    num_payments = ct.c_ulong()
    num_observations = ct.c_ulong()
    error_buffer = make_bytes_buffer(error_buffer_size)

    den = ct.c_char_p(definition.encode(__encoding__))
    lic = ct.c_char_p(token.encode(__encoding__))

    status = ito_dimensions_func(den, len(definition),
                                 ct.byref(num_dates),
                                 ct.byref(max_date_properties_size),
                                 ct.byref(num_currencies),
                                 ct.byref(max_currency_properties_size),
                                 ct.byref(num_keys),
                                 ct.byref(max_key_properties_size),
                                 ct.byref(num_payments),
                                 ct.byref(num_observations),
                                 ct.c_ulong(max_executions),
                                 ct.c_ulong(memory_foot_print),
                                 error_buffer, error_buffer_size,
                                 lic, len(token))
    error_handler(status, error_buffer, error_buffer_size)

    return (num_dates.value,
            max_date_properties_size.value,
            num_currencies.value,
            max_currency_properties_size.value,
            num_keys.value,
            max_key_properties_size.value,
            num_payments.value,
            num_observations.value)


def ito_properties(definition,
                   max_executions, memory_foot_print,
                   num_dates,
                   max_date_properties_size,
                   num_currencies,
                   max_currency_properties_size,
                   num_keys,
                   max_key_properties_size,
                   num_payments,
                   num_observations,
                   error_buffer_size,
                   token):
    error_buffer = make_bytes_buffer(error_buffer_size)
    dates_buffer = make_chars_buffer(num_dates * (max_date_properties_size + 1))
    currencies_buffer = make_chars_buffer(num_currencies * (max_currency_properties_size + 1))
    keys_buffer = make_chars_buffer(num_keys * (max_key_properties_size + 1))

    payment_dates_buffer = make_ints_buffer(num_payments)
    payment_currencies_buffer = make_ints_buffer(num_payments)
    payment_directions_buffer = make_bools_buffer(num_payments)
    payment_determination_dates_buffer = make_ints_buffer(num_payments)

    payments_to_observations_buffer = make_ints_buffer(num_payments * num_observations)
    observation_dates_buffer = make_ints_buffer(num_observations)
    observation_keys_buffer = make_ints_buffer(num_observations)

    den = ct.c_char_p(definition.encode(__encoding__))
    lic = ct.c_char_p(token.encode(__encoding__))

    status = ito_properties_func(den, len(definition),
                                 dates_buffer,
                                 currencies_buffer,
                                 keys_buffer,
                                 payment_dates_buffer,
                                 payment_currencies_buffer,
                                 payment_directions_buffer,
                                 payment_determination_dates_buffer,
                                 observation_dates_buffer,
                                 observation_keys_buffer,
                                 payments_to_observations_buffer,
                                 ct.c_ulong(max_executions),
                                 ct.c_ulong(memory_foot_print),
                                 error_buffer, error_buffer_size,
                                 lic, len(token))

    error_handler(status, error_buffer, error_buffer_size)

    dates = extract(dates_buffer, max_date_properties_size + 1)
    currencies = extract(currencies_buffer, max_currency_properties_size + 1)
    keys = extract(keys_buffer, max_key_properties_size + 1)

    return (dates, currencies, keys, list(payment_dates_buffer), list(payment_currencies_buffer), list(
        payment_directions_buffer), list(observation_keys_buffer), list(observation_dates_buffer))


def ito_payments(definition,
                 num_paths,
                 num_payments,
                 observations,
                 max_executions, memory_foot_print,
                 error_buffer_size,
                 token):
    den = ct.c_char_p(definition.encode(__encoding__))
    lic = ct.c_char_p(token.encode(__encoding__))

    payments_data = make_floats_buffer(num_paths * num_payments)
    error_buffer = make_bytes_buffer(error_buffer_size)
    status = ito_payments_func(den, len(definition),
                               ct.c_ulong(num_paths), observations, payments_data,
                               ct.c_ulong(max_executions), ct.c_ulong(memory_foot_print),
                               error_buffer, error_buffer_size,
                               lic, len(token))

    error_handler(status, error_buffer, error_buffer_size)
    return payments_data


def ito_payments_with_gradients(definition,
                                num_paths,
                                num_payments,
                                num_observations,
                                observations,
                                payment_adjoints,
                                max_executions, memory_foot_print,
                                error_buffer_size,
                                token):
    den = ct.c_char_p(definition.encode(__encoding__))
    lic = ct.c_char_p(token.encode(__encoding__))

    payments_data = make_floats_buffer(num_paths * num_payments)
    observation_adjoints_data = make_floats_buffer(num_paths * num_observations)
    error_buffer = make_bytes_buffer(error_buffer_size)
    status = ito_payments_with_gradients_func(den, len(definition),
                                              ct.c_ulong(num_paths), observations, payment_adjoints,
                                              payments_data, observation_adjoints_data,
                                              ct.c_ulong(max_executions), ct.c_ulong(memory_foot_print),
                                              error_buffer, error_buffer_size,
                                              lic, len(token))

    error_handler(status, error_buffer, error_buffer_size)
    return payments_data, observation_adjoints_data


def ito_num_errors(error):
    num_errors = ct.c_ulong()
    num_accessible_errors = ct.c_ulong()
    required_size = ct.c_ulong()
    ito_error_num_errors_func(error,
                              ct.byref(num_errors),
                              ct.byref(num_accessible_errors),
                              ct.byref(required_size))
    return num_errors.value, num_accessible_errors.value, required_size.value


def ito_error_code(error, idx):
    code = ct.c_int()
    ito_error_code_func(error, ct.c_ulong(idx), ct.byref(code))
    return code.value


def ito_error_path(error, idx):
    path = ct.c_ulong()
    ito_error_path_func(error, ct.c_ulong(idx), ct.byref(path))
    return path.value


def ito_error_message_size(error, idx):
    error_message_size = ct.c_ulong()
    ito_error_message_size_func(error, ct.c_ulong(idx), ct.byref(error_message_size))
    return error_message_size.value


def ito_error_message(error, idx, size):
    buffer = make_chars_buffer(size)
    ito_error_message_func(error, ct.c_ulong(idx), buffer)
    return buffer[0:size].decode(__encoding__).rstrip('\000')


def ito_error_num_positions(error, idx):
    num_positions = ct.c_ulong()
    ito_error_num_positions_func(error, ct.c_ulong(idx), ct.byref(num_positions))
    return num_positions.value


def ito_error_first_position(error, idx, idx_pos):
    first_position = ct.c_ulong()
    ito_error_first_position_func(error, ct.c_ulong(idx), ct.c_ulong(idx_pos), ct.byref(first_position))
    return first_position.value


def ito_error_first_line(error, idx, idx_pos):
    first_line = ct.c_ulong()
    ito_error_first_line_func(error, ct.c_ulong(idx), ct.c_ulong(idx_pos), ct.byref(first_line))
    return first_line.value


def ito_error_first_offset(error, idx, idx_pos):
    first_offset = ct.c_ulong()
    ito_error_first_offset_func(error, ct.c_ulong(idx), ct.c_ulong(idx_pos), ct.byref(first_offset))
    return first_offset.value


def ito_error_last_position(error, idx, idx_pos):
    last_position = ct.c_ulong()
    ito_error_last_position_func(error, ct.c_ulong(idx), ct.c_ulong(idx_pos), ct.byref(last_position))
    return last_position.value


def ito_error_last_line(error, idx, idx_pos):
    last_line = ct.c_ulong()
    ito_error_last_line_func(error, ct.c_ulong(idx), ct.c_ulong(idx_pos), ct.byref(last_line))
    return last_line.value


def ito_error_last_offset(error, idx, idx_pos):
    last_offset = ct.c_ulong()
    ito_error_last_offset_func(error, ct.c_ulong(idx), ct.c_ulong(idx_pos), ct.byref(last_offset))
    return last_offset.value


class Position:

    def __init__(self, pos, line_number, offset):
        self.pos = pos
        self.line_number = line_number
        self.offset = offset

    @staticmethod
    def message(positions):
        pass


class UserErrorInfo:

    def __init__(self, error_code, positions, what, path):
        self.error_code = error_code
        self.positions = positions
        self.what = what
        self.path = path

    @staticmethod
    def what(user_errors):
        pass


def position_message(positions):
    msg = ""
    for (first, last) in positions:
        msg += "line[" + str(first.line_number) + "], [" + str(first.offset) + "], "
        msg += "line[" + str(last.line_number) + "], [" + str(last.offset) + "])"
    return msg


def error_message(num_errors, required_size, error_infos):
    msg = "There are " + str(num_errors) + " errors, of which " + str(len(error_infos)) + " have been recorded."

    if len(error_infos) < num_errors:
        msg += ' Not all errors could be recorded, increase the size of the error buffer to at least ' + str(
            required_size) + "."

    for info in error_infos:
        msg += " Error at position[" + position_message(
            info.positions) + "], code[" + str(info.error_code) + "], [" + info.what + "], in batch[" + str(
            info.path) + "]."

    return msg


class Error(Exception):
    def __init__(self, message):
        super().__init__(message)


class UserError(Exception):
    def __init__(self, num_errors, required_size, error_infos):
        self.num_errors = num_errors
        self.required_size = required_size
        self.error_infos = error_infos

        super().__init__(error_message(num_errors, required_size, error_infos))


def extract_positions(error, idx, idx_pos):
    first_position = ito_error_first_position(error, idx, idx_pos)
    first_line = ito_error_first_line(error, idx, idx_pos)
    first_offset = ito_error_first_offset(error, idx, idx_pos)

    last_position = ito_error_last_position(error, idx, idx_pos)
    last_line = ito_error_last_line(error, idx, idx_pos)
    last_offset = ito_error_last_offset(error, idx, idx_pos)

    return Position(first_position, first_line, first_offset), Position(last_position, last_line, last_offset)


def on_error(error_buffer, error_buffer_size):
    num_errors, num_accessible_errors, required_size = ito_num_errors(error_buffer)

    errors = []
    for idx in range(num_accessible_errors):
        path = ito_error_path(error_buffer, idx)
        code = ito_error_code(error_buffer, idx)
        error_msg_size = ito_error_message_size(error_buffer, idx)
        error_msg = ito_error_message(error_buffer, idx, error_msg_size)
        num_positions = ito_error_num_positions(error_buffer, idx)

        positions = []
        for idx_pos in range(num_positions):
            positions.append(extract_positions(error_buffer, idx, idx_pos))

        errors.append(UserErrorInfo(code, positions, error_msg, path))
    raise UserError(num_errors, required_size, errors)


def error_handler(status, error_buffer, error_buffer_size):
    if status == 0:
        return
    elif status == 1:
        raise Error("An unknown error occurred.")
    elif status == 2:
        on_error(error_buffer, error_buffer_size)
    elif status == 3:
        raise Error("A system error occurred.")
    elif status == 4:
        raise Error("A library error occurred.")
    elif status == 5:
        raise Error("A licencing error occurred.")
    else:
        raise Error("An unrecognised error occurred.")


def list_to_array(a):
    size = len(a)
    return (ct.c_double * size)(*a)
