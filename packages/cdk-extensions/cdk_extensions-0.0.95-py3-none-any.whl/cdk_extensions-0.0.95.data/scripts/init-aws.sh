#!python

import jsii
import sys

__jsii_assembly__ = jsii.JSIIAssembly.load(
    "cdk-extensions", "0.0.95", "cdk_extensions", "cdk-extensions@0.0.95.jsii.tgz"
)

exit_code = __jsii_assembly__.invokeBinScript(
    "cdk-extensions", "init-aws.sh", sys.argv[1:]
)
exit(exit_code)
