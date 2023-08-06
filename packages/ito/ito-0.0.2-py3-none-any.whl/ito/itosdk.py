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

__token__ = """4f 41 45 53 01 02 0a 00 01 00 00 00 00 00 00 00 2a 78 42 21 a3 ff fa 78 16 0e 3e 98 e1 f8 29 09 31 82 b8 f7 98 ec b8 09 f4 bb 2a c6 0d 85 6a 14 74 7a 03 de 49 ef c5 cf 7a e7 18 f3 a9 44 59 20 fb 50 49 c5 89 80 6d c0 dd 73 00 19 fe f6 3b f8
"""


from functools import total_ordering

from . import itolib


@total_ordering
class ObservationDefinition:

    def __init__(self, key, date):
        self.key = key
        self.date = date

    def __eq__(self, other):
        return self.key == other.key and self.date == other.date

    def __lt__(self, other):
        # observations ordered by date then key
        if self.date != other.date:
            return self.date < other.date
        else:
            return self.key < other.key

    def __repr__(self):
        return self.date + "_" + self.key


@total_ordering
class PaymentDefinition:

    def __init__(self, is_pay_not_get, date, currency):
        self.is_pay_not_get = is_pay_not_get
        self.date = date
        self.currency = currency

    def __eq__(self, other):
        return self.is_pay_not_get == other.is_pay_not_get \
               and self.date == other.date \
               and self.currency == other.currency

    def __lt__(self, other):
        if self.is_pay_not_get != other.is_pay_not_get:
            return not self.is_pay_not_get
        elif self.date != other.date:
            return self.date < other.date
        else:
            return self.currency < other.currency

    def __hash__(self):
        payment_code = "pay" if self.is_pay_not_get else "get"
        return (payment_code + "_" + self.date + "_" + self.currency).__hash__()

    def __repr__(self):
        payment_code = "pay" if self.is_pay_not_get else "get"
        return payment_code + "_" + self.date + "_" + self.currency


class Handle:
    def __init__(self, definition, licence=__token__,
                 max_executions=100000,
                 memory_footprint=10000,
                 error_buffer_size=1000):
        self.definition = definition
        self.licence = licence
        self.max_executions = max_executions
        self.memory_footprint = memory_footprint
        self.error_buffer_size = error_buffer_size

        self.dates = None
        self.currencies = None
        self.keys = None

        self.payment_definitions = None
        self.observation_definitions = None

        self.num_payments = None
        self.num_observations = None

        (num_dates,
         max_date_properties_size,
         num_currencies,
         max_currency_properties_size,
         num_keys,
         max_key_properties_size,
         self.num_payments,
         self.num_observations) = itolib.ito_dimensions(self.definition,
                                                        self.max_executions, self.memory_footprint,
                                                        self.error_buffer_size,
                                                        self.licence)

        (self.dates, self.currencies, self.keys,
         payment_dates, payment_currencies, payment_directions,
         observation_keys, observation_dates) = itolib.ito_properties(self.definition,
                                                                      self.max_executions,
                                                                      self.memory_footprint,
                                                                      num_dates,
                                                                      max_date_properties_size,
                                                                      num_currencies,
                                                                      max_currency_properties_size,
                                                                      num_keys,
                                                                      max_key_properties_size,
                                                                      self.num_payments,
                                                                      self.num_observations,
                                                                      self.error_buffer_size,
                                                                      self.licence)

        self.payment_definitions = [PaymentDefinition(direction, self.dates[date], self.currencies[currency])
                                    for date, currency, direction in
                                    zip(payment_dates, payment_currencies, payment_directions)]

        self.observation_definitions = [ObservationDefinition(self.keys[key], self.dates[date]) for key, date in
                                        zip(observation_keys, observation_dates)]

    def compute_payments(self, num_paths, observations):
        return itolib.ito_payments(self.definition,
                                   num_paths,
                                   len(self.payment_definitions),
                                   itolib.list_to_array(observations),
                                   self.max_executions, self.memory_footprint,
                                   self.error_buffer_size,
                                   self.licence)

    def compute_payments_with_gradients(self, num_paths, observations, payment_adjoints):
        payments, observation_adjoints = itolib.ito_payments_with_gradients(self.definition,
                                                                            num_paths,
                                                                            len(self.payment_definitions),
                                                                            len(self.observation_definitions),
                                                                            itolib.list_to_array(observations),
                                                                            itolib.list_to_array(payment_adjoints),
                                                                            self.max_executions, self.memory_footprint,
                                                                            self.error_buffer_size,
                                                                            self.licence)
        return payments, observation_adjoints

    def find_observation(self, key, date):
        ret = None
        try:
            ret = self.observation_definitions.index(ObservationDefinition(key, date))
        except ValueError:
            pass
        return ret
