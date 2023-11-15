import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_config as _aws_cdk_aws_config_ceddda9d
import constructs as _constructs_77d1e7e8
from ..ssm import IAutomationDocument as _IAutomationDocument_1b1403a3


@jsii.data_type(
    jsii_type="cdk-extensions.config.AutomationDocumentRemediationProps",
    jsii_struct_bases=[],
    name_mapping={
        "document": "document",
        "concurrency_percentage": "concurrencyPercentage",
        "error_percentage": "errorPercentage",
        "version": "version",
    },
)
class AutomationDocumentRemediationProps:
    def __init__(
        self,
        *,
        document: _IAutomationDocument_1b1403a3,
        concurrency_percentage: typing.Optional[jsii.Number] = None,
        error_percentage: typing.Optional[jsii.Number] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param document: 
        :param concurrency_percentage: 
        :param error_percentage: 
        :param version: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41fd093f7815e6bb4975f0bb5e0d065656a8fec3e38553cf16c6b6e2146067fc)
            check_type(argname="argument document", value=document, expected_type=type_hints["document"])
            check_type(argname="argument concurrency_percentage", value=concurrency_percentage, expected_type=type_hints["concurrency_percentage"])
            check_type(argname="argument error_percentage", value=error_percentage, expected_type=type_hints["error_percentage"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "document": document,
        }
        if concurrency_percentage is not None:
            self._values["concurrency_percentage"] = concurrency_percentage
        if error_percentage is not None:
            self._values["error_percentage"] = error_percentage
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def document(self) -> _IAutomationDocument_1b1403a3:
        result = self._values.get("document")
        assert result is not None, "Required property 'document' is missing"
        return typing.cast(_IAutomationDocument_1b1403a3, result)

    @builtins.property
    def concurrency_percentage(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("concurrency_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def error_percentage(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("error_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutomationDocumentRemediationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="cdk-extensions.config.IRemediationConfiguration")
class IRemediationConfiguration(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="remediationConfigurationArn")
    def remediation_configuration_arn(self) -> builtins.str:
        ...

    @builtins.property
    @jsii.member(jsii_name="remediationConfigurationName")
    def remediation_configuration_name(self) -> builtins.str:
        ...


class _IRemediationConfigurationProxy:
    __jsii_type__: typing.ClassVar[str] = "cdk-extensions.config.IRemediationConfiguration"

    @builtins.property
    @jsii.member(jsii_name="remediationConfigurationArn")
    def remediation_configuration_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remediationConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="remediationConfigurationName")
    def remediation_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remediationConfigurationName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRemediationConfiguration).__jsii_proxy_class__ = lambda : _IRemediationConfigurationProxy


@jsii.interface(jsii_type="cdk-extensions.config.IRemediationTarget")
class IRemediationTarget(typing_extensions.Protocol):
    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.IConstruct,
    ) -> "RemediationTargetConfiguration":
        '''
        :param scope: -
        '''
        ...


class _IRemediationTargetProxy:
    __jsii_type__: typing.ClassVar[str] = "cdk-extensions.config.IRemediationTarget"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.IConstruct,
    ) -> "RemediationTargetConfiguration":
        '''
        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a456e8a1877116596bc2a8dbaa2cf16cd6330d067bfc6a628cfa86517843e1b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("RemediationTargetConfiguration", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRemediationTarget).__jsii_proxy_class__ = lambda : _IRemediationTargetProxy


@jsii.implements(IRemediationConfiguration)
class RemediationConfiguration(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-extensions.config.RemediationConfiguration",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        *,
        config_rule: _aws_cdk_aws_config_ceddda9d.IRule,
        static_parameters: typing.Mapping[builtins.str, typing.Sequence[typing.Any]],
        target: IRemediationTarget,
        automatic: typing.Optional[builtins.bool] = None,
        maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
        resource_parameter: typing.Optional[builtins.str] = None,
        resource_type: typing.Optional[builtins.str] = None,
        retry_interval: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param config_rule: 
        :param static_parameters: 
        :param target: 
        :param automatic: 
        :param maximum_automatic_attempts: 
        :param resource_parameter: 
        :param resource_type: 
        :param retry_interval: 
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be63182f5c4626507a0c5ea0d934096a80791412af4fedc8c0e439c9f4eb084)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RemediationConfigurationProps(
            config_rule=config_rule,
            static_parameters=static_parameters,
            target=target,
            automatic=automatic,
            maximum_automatic_attempts=maximum_automatic_attempts,
            resource_parameter=resource_parameter,
            resource_type=resource_type,
            retry_interval=retry_interval,
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromRemediationConfigurationArn")
    @builtins.classmethod
    def from_remediation_configuration_arn(
        cls,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        arn: builtins.str,
    ) -> IRemediationConfiguration:
        '''
        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca6047b8f85f056bbb3f2063cf1ecebd4eda1c5f0498cd22eccef3650dbbf638)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast(IRemediationConfiguration, jsii.sinvoke(cls, "fromRemediationConfigurationArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromRemediationConfigurationAttributes")
    @builtins.classmethod
    def from_remediation_configuration_attributes(
        cls,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        *,
        arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> IRemediationConfiguration:
        '''
        :param scope: -
        :param id: -
        :param arn: 
        :param name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e871607e80b2fef46e71e90a7bba5adf019fcd0fa4a5cffcc64b0f800d2a547)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = RemediationConfigurationAttributes(arn=arn, name=name)

        return typing.cast(IRemediationConfiguration, jsii.sinvoke(cls, "fromRemediationConfigurationAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromRemediationConfigurationName")
    @builtins.classmethod
    def from_remediation_configuration_name(
        cls,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        name: builtins.str,
    ) -> IRemediationConfiguration:
        '''
        :param scope: -
        :param id: -
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e35e6d585e1260c3341ed60b2c7530ca26cc297469dfa9d94257707d03454d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(IRemediationConfiguration, jsii.sinvoke(cls, "fromRemediationConfigurationName", [scope, id, name]))

    @jsii.member(jsii_name="addParameter")
    def add_parameter(self, key: builtins.str, *values: builtins.str) -> None:
        '''
        :param key: -
        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f3a35325b11f74ac4eb3308e8e4fb71618fa82d65a5f7238bf18515360b60c2)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=typing.Tuple[type_hints["values"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addParameter", [key, *values]))

    @jsii.member(jsii_name="renderParameters")
    def _render_parameters(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.invoke(self, "renderParameters", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ARN_FORMAT")
    def ARN_FORMAT(cls) -> _aws_cdk_ceddda9d.ArnFormat:
        return typing.cast(_aws_cdk_ceddda9d.ArnFormat, jsii.sget(cls, "ARN_FORMAT"))

    @builtins.property
    @jsii.member(jsii_name="configRule")
    def config_rule(self) -> _aws_cdk_aws_config_ceddda9d.IRule:
        return typing.cast(_aws_cdk_aws_config_ceddda9d.IRule, jsii.get(self, "configRule"))

    @builtins.property
    @jsii.member(jsii_name="remediationConfigurationArn")
    def remediation_configuration_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remediationConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="remediationConfigurationName")
    def remediation_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remediationConfigurationName"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> _aws_cdk_aws_config_ceddda9d.CfnRemediationConfiguration:
        return typing.cast(_aws_cdk_aws_config_ceddda9d.CfnRemediationConfiguration, jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="automatic")
    def automatic(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "automatic"))

    @builtins.property
    @jsii.member(jsii_name="maximumAutomaticAttempts")
    def maximum_automatic_attempts(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumAutomaticAttempts"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="retryInterval")
    def retry_interval(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], jsii.get(self, "retryInterval"))


@jsii.data_type(
    jsii_type="cdk-extensions.config.RemediationConfigurationAttributes",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "name": "name"},
)
class RemediationConfigurationAttributes:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: 
        :param name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__658cfba4d97262b7046aae62278554e1ce54b362db2588cc6471e427ee747854)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemediationConfigurationAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-extensions.config.RemediationConfigurationProps",
    jsii_struct_bases=[_aws_cdk_ceddda9d.ResourceProps],
    name_mapping={
        "account": "account",
        "environment_from_arn": "environmentFromArn",
        "physical_name": "physicalName",
        "region": "region",
        "config_rule": "configRule",
        "static_parameters": "staticParameters",
        "target": "target",
        "automatic": "automatic",
        "maximum_automatic_attempts": "maximumAutomaticAttempts",
        "resource_parameter": "resourceParameter",
        "resource_type": "resourceType",
        "retry_interval": "retryInterval",
    },
)
class RemediationConfigurationProps(_aws_cdk_ceddda9d.ResourceProps):
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        config_rule: _aws_cdk_aws_config_ceddda9d.IRule,
        static_parameters: typing.Mapping[builtins.str, typing.Sequence[typing.Any]],
        target: IRemediationTarget,
        automatic: typing.Optional[builtins.bool] = None,
        maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
        resource_parameter: typing.Optional[builtins.str] = None,
        resource_type: typing.Optional[builtins.str] = None,
        retry_interval: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    ) -> None:
        '''
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        :param config_rule: 
        :param static_parameters: 
        :param target: 
        :param automatic: 
        :param maximum_automatic_attempts: 
        :param resource_parameter: 
        :param resource_type: 
        :param retry_interval: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5efb78a5833f4622608a5a76f2c06b1c3de04574f39b2f5d61745c41c5abe382)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument environment_from_arn", value=environment_from_arn, expected_type=type_hints["environment_from_arn"])
            check_type(argname="argument physical_name", value=physical_name, expected_type=type_hints["physical_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument config_rule", value=config_rule, expected_type=type_hints["config_rule"])
            check_type(argname="argument static_parameters", value=static_parameters, expected_type=type_hints["static_parameters"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
            check_type(argname="argument maximum_automatic_attempts", value=maximum_automatic_attempts, expected_type=type_hints["maximum_automatic_attempts"])
            check_type(argname="argument resource_parameter", value=resource_parameter, expected_type=type_hints["resource_parameter"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument retry_interval", value=retry_interval, expected_type=type_hints["retry_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_rule": config_rule,
            "static_parameters": static_parameters,
            "target": target,
        }
        if account is not None:
            self._values["account"] = account
        if environment_from_arn is not None:
            self._values["environment_from_arn"] = environment_from_arn
        if physical_name is not None:
            self._values["physical_name"] = physical_name
        if region is not None:
            self._values["region"] = region
        if automatic is not None:
            self._values["automatic"] = automatic
        if maximum_automatic_attempts is not None:
            self._values["maximum_automatic_attempts"] = maximum_automatic_attempts
        if resource_parameter is not None:
            self._values["resource_parameter"] = resource_parameter
        if resource_type is not None:
            self._values["resource_type"] = resource_type
        if retry_interval is not None:
            self._values["retry_interval"] = retry_interval

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID this resource belongs to.

        :default: - the resource is in the same account as the stack it belongs to
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_from_arn(self) -> typing.Optional[builtins.str]:
        '''ARN to deduce region and account from.

        The ARN is parsed and the account and region are taken from the ARN.
        This should be used for imported resources.

        Cannot be supplied together with either ``account`` or ``region``.

        :default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        '''
        result = self._values.get("environment_from_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def physical_name(self) -> typing.Optional[builtins.str]:
        '''The value passed in by users to the physical name prop of the resource.

        - ``undefined`` implies that a physical name will be allocated by
          CloudFormation during deployment.
        - a concrete value implies a specific physical name
        - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated
          by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation.

        :default: - The physical name will be allocated by CloudFormation at deployment time
        '''
        result = self._values.get("physical_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region this resource belongs to.

        :default: - the resource is in the same region as the stack it belongs to
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_rule(self) -> _aws_cdk_aws_config_ceddda9d.IRule:
        result = self._values.get("config_rule")
        assert result is not None, "Required property 'config_rule' is missing"
        return typing.cast(_aws_cdk_aws_config_ceddda9d.IRule, result)

    @builtins.property
    def static_parameters(
        self,
    ) -> typing.Mapping[builtins.str, typing.List[typing.Any]]:
        result = self._values.get("static_parameters")
        assert result is not None, "Required property 'static_parameters' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.List[typing.Any]], result)

    @builtins.property
    def target(self) -> IRemediationTarget:
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(IRemediationTarget, result)

    @builtins.property
    def automatic(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("automatic")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def maximum_automatic_attempts(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("maximum_automatic_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_parameter(self) -> typing.Optional[builtins.str]:
        result = self._values.get("resource_parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_interval(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        result = self._values.get("retry_interval")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemediationConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RemediationTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-extensions.config.RemediationTarget",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="automationDocument")
    @builtins.classmethod
    def automation_document(
        cls,
        *,
        document: _IAutomationDocument_1b1403a3,
        concurrency_percentage: typing.Optional[jsii.Number] = None,
        error_percentage: typing.Optional[jsii.Number] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> IRemediationTarget:
        '''
        :param document: 
        :param concurrency_percentage: 
        :param error_percentage: 
        :param version: 
        '''
        props = AutomationDocumentRemediationProps(
            document=document,
            concurrency_percentage=concurrency_percentage,
            error_percentage=error_percentage,
            version=version,
        )

        return typing.cast(IRemediationTarget, jsii.sinvoke(cls, "automationDocument", [props]))


@jsii.data_type(
    jsii_type="cdk-extensions.config.RemediationTargetConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "target_id": "targetId",
        "target_type": "targetType",
        "controls": "controls",
        "target_version": "targetVersion",
    },
)
class RemediationTargetConfiguration:
    def __init__(
        self,
        *,
        target_id: builtins.str,
        target_type: "RemediationTargetType",
        controls: typing.Optional[typing.Union[_aws_cdk_aws_config_ceddda9d.CfnRemediationConfiguration.ExecutionControlsProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        target_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_id: 
        :param target_type: 
        :param controls: 
        :param target_version: 
        '''
        if isinstance(controls, dict):
            controls = _aws_cdk_aws_config_ceddda9d.CfnRemediationConfiguration.ExecutionControlsProperty(**controls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1073792167c111bd0f9831baaa03ebef02da5c232064994b2a08b8ed6c0401bf)
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            check_type(argname="argument controls", value=controls, expected_type=type_hints["controls"])
            check_type(argname="argument target_version", value=target_version, expected_type=type_hints["target_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_id": target_id,
            "target_type": target_type,
        }
        if controls is not None:
            self._values["controls"] = controls
        if target_version is not None:
            self._values["target_version"] = target_version

    @builtins.property
    def target_id(self) -> builtins.str:
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> "RemediationTargetType":
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast("RemediationTargetType", result)

    @builtins.property
    def controls(
        self,
    ) -> typing.Optional[_aws_cdk_aws_config_ceddda9d.CfnRemediationConfiguration.ExecutionControlsProperty]:
        result = self._values.get("controls")
        return typing.cast(typing.Optional[_aws_cdk_aws_config_ceddda9d.CfnRemediationConfiguration.ExecutionControlsProperty], result)

    @builtins.property
    def target_version(self) -> typing.Optional[builtins.str]:
        result = self._values.get("target_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemediationTargetConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RemediationTargetType(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-extensions.config.RemediationTargetType",
):
    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, value: builtins.str) -> "RemediationTargetType":
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d26553cdeef81403b1c8c3e71aa9f2f9cb17fb9131449baa058bff396fb0e71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("RemediationTargetType", jsii.sinvoke(cls, "of", [value]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SSM_DOCUMENT")
    def SSM_DOCUMENT(cls) -> "RemediationTargetType":
        return typing.cast("RemediationTargetType", jsii.sget(cls, "SSM_DOCUMENT"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))


__all__ = [
    "AutomationDocumentRemediationProps",
    "IRemediationConfiguration",
    "IRemediationTarget",
    "RemediationConfiguration",
    "RemediationConfigurationAttributes",
    "RemediationConfigurationProps",
    "RemediationTarget",
    "RemediationTargetConfiguration",
    "RemediationTargetType",
]

publication.publish()

def _typecheckingstub__41fd093f7815e6bb4975f0bb5e0d065656a8fec3e38553cf16c6b6e2146067fc(
    *,
    document: _IAutomationDocument_1b1403a3,
    concurrency_percentage: typing.Optional[jsii.Number] = None,
    error_percentage: typing.Optional[jsii.Number] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a456e8a1877116596bc2a8dbaa2cf16cd6330d067bfc6a628cfa86517843e1b(
    scope: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be63182f5c4626507a0c5ea0d934096a80791412af4fedc8c0e439c9f4eb084(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    *,
    config_rule: _aws_cdk_aws_config_ceddda9d.IRule,
    static_parameters: typing.Mapping[builtins.str, typing.Sequence[typing.Any]],
    target: IRemediationTarget,
    automatic: typing.Optional[builtins.bool] = None,
    maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
    resource_parameter: typing.Optional[builtins.str] = None,
    resource_type: typing.Optional[builtins.str] = None,
    retry_interval: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca6047b8f85f056bbb3f2063cf1ecebd4eda1c5f0498cd22eccef3650dbbf638(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e871607e80b2fef46e71e90a7bba5adf019fcd0fa4a5cffcc64b0f800d2a547(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    *,
    arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e35e6d585e1260c3341ed60b2c7530ca26cc297469dfa9d94257707d03454d6(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3a35325b11f74ac4eb3308e8e4fb71618fa82d65a5f7238bf18515360b60c2(
    key: builtins.str,
    *values: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658cfba4d97262b7046aae62278554e1ce54b362db2588cc6471e427ee747854(
    *,
    arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5efb78a5833f4622608a5a76f2c06b1c3de04574f39b2f5d61745c41c5abe382(
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    config_rule: _aws_cdk_aws_config_ceddda9d.IRule,
    static_parameters: typing.Mapping[builtins.str, typing.Sequence[typing.Any]],
    target: IRemediationTarget,
    automatic: typing.Optional[builtins.bool] = None,
    maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
    resource_parameter: typing.Optional[builtins.str] = None,
    resource_type: typing.Optional[builtins.str] = None,
    retry_interval: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1073792167c111bd0f9831baaa03ebef02da5c232064994b2a08b8ed6c0401bf(
    *,
    target_id: builtins.str,
    target_type: RemediationTargetType,
    controls: typing.Optional[typing.Union[_aws_cdk_aws_config_ceddda9d.CfnRemediationConfiguration.ExecutionControlsProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    target_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d26553cdeef81403b1c8c3e71aa9f2f9cb17fb9131449baa058bff396fb0e71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
