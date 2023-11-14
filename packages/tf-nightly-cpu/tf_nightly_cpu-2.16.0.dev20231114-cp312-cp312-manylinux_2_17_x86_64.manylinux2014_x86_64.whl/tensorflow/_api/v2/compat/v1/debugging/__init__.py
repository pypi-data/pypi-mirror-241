# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator2/generator/generator.py script.
"""Public API for tf._api.v2.debugging namespace
"""

import sys as _sys

from tensorflow._api.v2.compat.v1.debugging import experimental
from tensorflow.python.ops.gen_array_ops import check_numerics # line: 950
from tensorflow.python.ops.gen_math_ops import is_finite # line: 4935
from tensorflow.python.ops.gen_math_ops import is_inf # line: 5031
from tensorflow.python.ops.gen_math_ops import is_nan # line: 5127
from tensorflow.python.debug.lib.check_numerics_callback import disable_check_numerics # line: 445
from tensorflow.python.debug.lib.check_numerics_callback import enable_check_numerics # line: 336
from tensorflow.python.eager.context import get_log_device_placement # line: 2546
from tensorflow.python.eager.context import set_log_device_placement # line: 2556
from tensorflow.python.ops.check_ops import assert_equal # line: 770
from tensorflow.python.ops.check_ops import assert_greater # line: 987
from tensorflow.python.ops.check_ops import assert_greater_equal # line: 1005
from tensorflow.python.ops.check_ops import assert_integer # line: 1448
from tensorflow.python.ops.check_ops import assert_less # line: 950
from tensorflow.python.ops.check_ops import assert_less_equal # line: 968
from tensorflow.python.ops.check_ops import assert_near # line: 858
from tensorflow.python.ops.check_ops import assert_negative # line: 576
from tensorflow.python.ops.check_ops import assert_non_negative # line: 685
from tensorflow.python.ops.check_ops import assert_non_positive # line: 741
from tensorflow.python.ops.check_ops import assert_none_equal # line: 792
from tensorflow.python.ops.check_ops import assert_positive # line: 630
from tensorflow.python.ops.check_ops import assert_proper_iterable # line: 511
from tensorflow.python.ops.check_ops import assert_rank # line: 1098
from tensorflow.python.ops.check_ops import assert_rank_at_least # line: 1196
from tensorflow.python.ops.check_ops import assert_rank_in # line: 1362
from tensorflow.python.ops.check_ops import assert_same_float_dtype # line: 2119
from tensorflow.python.ops.check_ops import assert_scalar # line: 2177
from tensorflow.python.ops.check_ops import assert_shapes # line: 1678
from tensorflow.python.ops.check_ops import assert_type # line: 1522
from tensorflow.python.ops.check_ops import is_non_decreasing # line: 1989
from tensorflow.python.ops.check_ops import is_numeric_tensor # line: 1954
from tensorflow.python.ops.check_ops import is_strictly_increasing # line: 2030
from tensorflow.python.ops.control_flow_assert import Assert # line: 62
from tensorflow.python.ops.numerics import verify_tensor_all_finite as assert_all_finite # line: 28
from tensorflow.python.util.traceback_utils import disable_traceback_filtering # line: 76
from tensorflow.python.util.traceback_utils import enable_traceback_filtering # line: 51
from tensorflow.python.util.traceback_utils import is_traceback_filtering_enabled # line: 32

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "debugging", public_apis=None, deprecation=False,
      has_lite=False)
