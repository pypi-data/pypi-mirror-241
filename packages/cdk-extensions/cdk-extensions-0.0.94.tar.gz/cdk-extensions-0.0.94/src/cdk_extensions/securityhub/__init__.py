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
import aws_cdk.aws_securityhub as _aws_cdk_aws_securityhub_ceddda9d
import constructs as _constructs_77d1e7e8


class ControlFindingGenerator(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-extensions.securityhub.ControlFindingGenerator",
):
    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, value: builtins.str) -> "ControlFindingGenerator":
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dc9e2a58fb824bbdaff26f70ae971ab9c58d8e9792263ae159d3e3660505c3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("ControlFindingGenerator", jsii.sinvoke(cls, "of", [value]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECURITY_CONTROL")
    def SECURITY_CONTROL(cls) -> "ControlFindingGenerator":
        return typing.cast("ControlFindingGenerator", jsii.sget(cls, "SECURITY_CONTROL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="STANDARD_CONTROL")
    def STANDARD_CONTROL(cls) -> "ControlFindingGenerator":
        return typing.cast("ControlFindingGenerator", jsii.sget(cls, "STANDARD_CONTROL"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="cdk-extensions.securityhub.DisableControlOptions",
    jsii_struct_bases=[],
    name_mapping={"reason": "reason"},
)
class DisableControlOptions:
    def __init__(self, *, reason: builtins.str) -> None:
        '''
        :param reason: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eb33f65c5a2a04dc60c5d474886c96a70ed706b653f8115cfb240ce61be5330)
            check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "reason": reason,
        }

    @builtins.property
    def reason(self) -> builtins.str:
        result = self._values.get("reason")
        assert result is not None, "Required property 'reason' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DisableControlOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-extensions.securityhub.HubAttributes",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "name": "name"},
)
class HubAttributes:
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
            type_hints = typing.get_type_hints(_typecheckingstub__68addb01464dff364f6c38095fe5cd60b696ed7936fc9baaf02405b323e853d1)
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
        return "HubAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-extensions.securityhub.HubProps",
    jsii_struct_bases=[_aws_cdk_ceddda9d.ResourceProps],
    name_mapping={
        "account": "account",
        "environment_from_arn": "environmentFromArn",
        "physical_name": "physicalName",
        "region": "region",
        "auto_enable_controls": "autoEnableControls",
        "consolidated_findings": "consolidatedFindings",
        "enable_default_standards": "enableDefaultStandards",
    },
)
class HubProps(_aws_cdk_ceddda9d.ResourceProps):
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        auto_enable_controls: typing.Optional[builtins.bool] = None,
        consolidated_findings: typing.Optional[builtins.bool] = None,
        enable_default_standards: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        :param auto_enable_controls: 
        :param consolidated_findings: 
        :param enable_default_standards: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__452bb749ef087cc5e37c4fbfa574a9fff196d1b676f597f0f1df9f11f635ae84)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument environment_from_arn", value=environment_from_arn, expected_type=type_hints["environment_from_arn"])
            check_type(argname="argument physical_name", value=physical_name, expected_type=type_hints["physical_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument auto_enable_controls", value=auto_enable_controls, expected_type=type_hints["auto_enable_controls"])
            check_type(argname="argument consolidated_findings", value=consolidated_findings, expected_type=type_hints["consolidated_findings"])
            check_type(argname="argument enable_default_standards", value=enable_default_standards, expected_type=type_hints["enable_default_standards"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if environment_from_arn is not None:
            self._values["environment_from_arn"] = environment_from_arn
        if physical_name is not None:
            self._values["physical_name"] = physical_name
        if region is not None:
            self._values["region"] = region
        if auto_enable_controls is not None:
            self._values["auto_enable_controls"] = auto_enable_controls
        if consolidated_findings is not None:
            self._values["consolidated_findings"] = consolidated_findings
        if enable_default_standards is not None:
            self._values["enable_default_standards"] = enable_default_standards

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
    def auto_enable_controls(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("auto_enable_controls")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def consolidated_findings(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("consolidated_findings")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_default_standards(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("enable_default_standards")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HubProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="cdk-extensions.securityhub.IHub")
class IHub(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="hubArn")
    def hub_arn(self) -> builtins.str:
        ...

    @builtins.property
    @jsii.member(jsii_name="hubName")
    def hub_name(self) -> builtins.str:
        ...


class _IHubProxy:
    __jsii_type__: typing.ClassVar[str] = "cdk-extensions.securityhub.IHub"

    @builtins.property
    @jsii.member(jsii_name="hubArn")
    def hub_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hubArn"))

    @builtins.property
    @jsii.member(jsii_name="hubName")
    def hub_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hubName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHub).__jsii_proxy_class__ = lambda : _IHubProxy


@jsii.interface(jsii_type="cdk-extensions.securityhub.IStandard")
class IStandard(_aws_cdk_ceddda9d.IResource, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="standardArn")
    def standard_arn(self) -> builtins.str:
        ...


class _IStandardProxy(
    jsii.proxy_for(_aws_cdk_ceddda9d.IResource), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "cdk-extensions.securityhub.IStandard"

    @builtins.property
    @jsii.member(jsii_name="standardArn")
    def standard_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "standardArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStandard).__jsii_proxy_class__ = lambda : _IStandardProxy


class RuleSet(metaclass=jsii.JSIIMeta, jsii_type="cdk-extensions.securityhub.RuleSet"):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.IConstruct) -> "ScopedRuleSet":
        '''
        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca2e7855760a599289ca11e96d35247402b992e0c053c7387daf73ecb37ac736)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("ScopedRuleSet", jsii.invoke(self, "bind", [scope]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ARN_FORMAT")
    def ARN_FORMAT(cls) -> _aws_cdk_ceddda9d.ArnFormat:
        return typing.cast(_aws_cdk_ceddda9d.ArnFormat, jsii.sget(cls, "ARN_FORMAT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CIS_FOUNDATIONS_1_2_0")
    def CIS_FOUNDATIONS_1_2_0(cls) -> "RuleSet":
        return typing.cast("RuleSet", jsii.sget(cls, "CIS_FOUNDATIONS_1_2_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CIS_FOUNDATIONS_1_4_0")
    def CIS_FOUNDATIONS_1_4_0(cls) -> "RuleSet":
        return typing.cast("RuleSet", jsii.sget(cls, "CIS_FOUNDATIONS_1_4_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FOUNDATIONAL_BEST_PRACTICES_1_0_0")
    def FOUNDATIONAL_BEST_PRACTICES_1_0_0(cls) -> "RuleSet":
        return typing.cast("RuleSet", jsii.sget(cls, "FOUNDATIONAL_BEST_PRACTICES_1_0_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NIST_800_53_5_0_0")
    def NIST_800_53_5_0_0(cls) -> "RuleSet":
        return typing.cast("RuleSet", jsii.sget(cls, "NIST_800_53_5_0_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PCI_DSS_3_2_1")
    def PCI_DSS_3_2_1(cls) -> "RuleSet":
        return typing.cast("RuleSet", jsii.sget(cls, "PCI_DSS_3_2_1"))


@jsii.data_type(
    jsii_type="cdk-extensions.securityhub.RuleSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "version": "version",
        "default": "default",
        "description": "description",
        "global_": "global",
        "name": "name",
    },
)
class RuleSetProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        version: builtins.str,
        default: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        global_: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: 
        :param version: 
        :param default: 
        :param description: 
        :param global_: 
        :param name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1228eafb92d45073a47db03b46340ff9e19d3af046743a77a9b31e001202472)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument global_", value=global_, expected_type=type_hints["global_"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "version": version,
        }
        if default is not None:
            self._values["default"] = default
        if description is not None:
            self._values["description"] = description
        if global_ is not None:
            self._values["global_"] = global_
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> builtins.str:
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("global_")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-extensions.securityhub.ScopedRuleSet",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "id": "id",
        "version": "version",
        "default": "default",
        "description": "description",
        "name": "name",
    },
)
class ScopedRuleSet:
    def __init__(
        self,
        *,
        arn: builtins.str,
        id: builtins.str,
        version: builtins.str,
        default: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: 
        :param id: 
        :param version: 
        :param default: 
        :param description: 
        :param name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ab47635ebd14eaf5055ad7bcd001641572d5ad454a12e1f57fa0f2fe41f9620)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
            "id": id,
            "version": version,
        }
        if default is not None:
            self._values["default"] = default
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def arn(self) -> builtins.str:
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        result = self._values.get("description")
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
        return "ScopedRuleSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStandard)
class Standard(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-extensions.securityhub.Standard",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        *,
        rule_set: RuleSet,
        disabled_controls: typing.Optional[typing.Sequence[builtins.str]] = None,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param rule_set: 
        :param disabled_controls: 
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7162a7ad4005bac732771c6731061a6b5a3adc361124a7469336425d6361f93d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StandardProps(
            rule_set=rule_set,
            disabled_controls=disabled_controls,
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromStandardArn")
    @builtins.classmethod
    def from_standard_arn(
        cls,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        arn: builtins.str,
    ) -> IStandard:
        '''
        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e00025604e562e64d2e9b48ce8e5cb33deea319fb8c519e88626ec5443e9e5a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast(IStandard, jsii.sinvoke(cls, "fromStandardArn", [scope, id, arn]))

    @jsii.member(jsii_name="disableControl")
    def disable_control(self, control: builtins.str, *, reason: builtins.str) -> None:
        '''
        :param control: -
        :param reason: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac7e4f64b5c88bdc348f34aaf832775f8bb3bd2d091a865c78ebd0310ceadecc)
            check_type(argname="argument control", value=control, expected_type=type_hints["control"])
        options = DisableControlOptions(reason=reason)

        return typing.cast(None, jsii.invoke(self, "disableControl", [control, options]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ARN_FORMAT")
    def ARN_FORMAT(cls) -> _aws_cdk_ceddda9d.ArnFormat:
        return typing.cast(_aws_cdk_ceddda9d.ArnFormat, jsii.sget(cls, "ARN_FORMAT"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> _aws_cdk_aws_securityhub_ceddda9d.CfnStandard:
        return typing.cast(_aws_cdk_aws_securityhub_ceddda9d.CfnStandard, jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="standardArn")
    def standard_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "standardArn"))


@jsii.data_type(
    jsii_type="cdk-extensions.securityhub.StandardProps",
    jsii_struct_bases=[_aws_cdk_ceddda9d.ResourceProps],
    name_mapping={
        "account": "account",
        "environment_from_arn": "environmentFromArn",
        "physical_name": "physicalName",
        "region": "region",
        "rule_set": "ruleSet",
        "disabled_controls": "disabledControls",
    },
)
class StandardProps(_aws_cdk_ceddda9d.ResourceProps):
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        rule_set: RuleSet,
        disabled_controls: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        :param rule_set: 
        :param disabled_controls: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ed0ee5eb24ada3c58a8db0b5e0a20cf712ca9250b61c3601c4ba16287af06ce)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument environment_from_arn", value=environment_from_arn, expected_type=type_hints["environment_from_arn"])
            check_type(argname="argument physical_name", value=physical_name, expected_type=type_hints["physical_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument rule_set", value=rule_set, expected_type=type_hints["rule_set"])
            check_type(argname="argument disabled_controls", value=disabled_controls, expected_type=type_hints["disabled_controls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_set": rule_set,
        }
        if account is not None:
            self._values["account"] = account
        if environment_from_arn is not None:
            self._values["environment_from_arn"] = environment_from_arn
        if physical_name is not None:
            self._values["physical_name"] = physical_name
        if region is not None:
            self._values["region"] = region
        if disabled_controls is not None:
            self._values["disabled_controls"] = disabled_controls

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
    def rule_set(self) -> RuleSet:
        result = self._values.get("rule_set")
        assert result is not None, "Required property 'rule_set' is missing"
        return typing.cast(RuleSet, result)

    @builtins.property
    def disabled_controls(self) -> typing.Optional[typing.List[builtins.str]]:
        result = self._values.get("disabled_controls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StandardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IHub)
class Hub(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-extensions.securityhub.Hub",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        *,
        auto_enable_controls: typing.Optional[builtins.bool] = None,
        consolidated_findings: typing.Optional[builtins.bool] = None,
        enable_default_standards: typing.Optional[builtins.bool] = None,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param auto_enable_controls: 
        :param consolidated_findings: 
        :param enable_default_standards: 
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b1200ba6e9faa36bd6059825334747a8ffdf5763b7983b3c3c82d2f3174c0ae)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = HubProps(
            auto_enable_controls=auto_enable_controls,
            consolidated_findings=consolidated_findings,
            enable_default_standards=enable_default_standards,
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromHubArn")
    @builtins.classmethod
    def from_hub_arn(
        cls,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        arn: builtins.str,
    ) -> IHub:
        '''
        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a3c7c6540108c38734811d36ebf44cea2082245c0349951fa802fe5d0bf242a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast(IHub, jsii.sinvoke(cls, "fromHubArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromHubAttributes")
    @builtins.classmethod
    def from_hub_attributes(
        cls,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        *,
        arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> IHub:
        '''
        :param scope: -
        :param id: -
        :param arn: 
        :param name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f533d6913d8b417508c076b8a2f6976f51212d31752f3a38283df8a4aa07140)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = HubAttributes(arn=arn, name=name)

        return typing.cast(IHub, jsii.sinvoke(cls, "fromHubAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromHubName")
    @builtins.classmethod
    def from_hub_name(
        cls,
        scope: _constructs_77d1e7e8.IConstruct,
        id: builtins.str,
        name: builtins.str,
    ) -> IHub:
        '''
        :param scope: -
        :param id: -
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b57d3b22d5b272da8e79438c6b00ec488820202a92c8f03c50479475841f4707)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(IHub, jsii.sinvoke(cls, "fromHubName", [scope, id, name]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ARN_FORMAT")
    def ARN_FORMAT(cls) -> _aws_cdk_ceddda9d.ArnFormat:
        return typing.cast(_aws_cdk_ceddda9d.ArnFormat, jsii.sget(cls, "ARN_FORMAT"))

    @builtins.property
    @jsii.member(jsii_name="hubArn")
    def hub_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hubArn"))

    @builtins.property
    @jsii.member(jsii_name="hubName")
    def hub_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hubName"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> _aws_cdk_aws_securityhub_ceddda9d.CfnHub:
        return typing.cast(_aws_cdk_aws_securityhub_ceddda9d.CfnHub, jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="autoEnableControls")
    def auto_enable_controls(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "autoEnableControls"))

    @builtins.property
    @jsii.member(jsii_name="consolidatedFindings")
    def consolidated_findings(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "consolidatedFindings"))

    @builtins.property
    @jsii.member(jsii_name="controlFindingGenerator")
    def control_finding_generator(self) -> typing.Optional[ControlFindingGenerator]:
        return typing.cast(typing.Optional[ControlFindingGenerator], jsii.get(self, "controlFindingGenerator"))

    @builtins.property
    @jsii.member(jsii_name="enableDefaultStandards")
    def enable_default_standards(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableDefaultStandards"))


__all__ = [
    "ControlFindingGenerator",
    "DisableControlOptions",
    "Hub",
    "HubAttributes",
    "HubProps",
    "IHub",
    "IStandard",
    "RuleSet",
    "RuleSetProps",
    "ScopedRuleSet",
    "Standard",
    "StandardProps",
]

publication.publish()

def _typecheckingstub__6dc9e2a58fb824bbdaff26f70ae971ab9c58d8e9792263ae159d3e3660505c3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eb33f65c5a2a04dc60c5d474886c96a70ed706b653f8115cfb240ce61be5330(
    *,
    reason: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68addb01464dff364f6c38095fe5cd60b696ed7936fc9baaf02405b323e853d1(
    *,
    arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__452bb749ef087cc5e37c4fbfa574a9fff196d1b676f597f0f1df9f11f635ae84(
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    auto_enable_controls: typing.Optional[builtins.bool] = None,
    consolidated_findings: typing.Optional[builtins.bool] = None,
    enable_default_standards: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca2e7855760a599289ca11e96d35247402b992e0c053c7387daf73ecb37ac736(
    scope: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1228eafb92d45073a47db03b46340ff9e19d3af046743a77a9b31e001202472(
    *,
    id: builtins.str,
    version: builtins.str,
    default: typing.Optional[builtins.bool] = None,
    description: typing.Optional[builtins.str] = None,
    global_: typing.Optional[builtins.bool] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ab47635ebd14eaf5055ad7bcd001641572d5ad454a12e1f57fa0f2fe41f9620(
    *,
    arn: builtins.str,
    id: builtins.str,
    version: builtins.str,
    default: typing.Optional[builtins.bool] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7162a7ad4005bac732771c6731061a6b5a3adc361124a7469336425d6361f93d(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    *,
    rule_set: RuleSet,
    disabled_controls: typing.Optional[typing.Sequence[builtins.str]] = None,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00025604e562e64d2e9b48ce8e5cb33deea319fb8c519e88626ec5443e9e5a1(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac7e4f64b5c88bdc348f34aaf832775f8bb3bd2d091a865c78ebd0310ceadecc(
    control: builtins.str,
    *,
    reason: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ed0ee5eb24ada3c58a8db0b5e0a20cf712ca9250b61c3601c4ba16287af06ce(
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    rule_set: RuleSet,
    disabled_controls: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b1200ba6e9faa36bd6059825334747a8ffdf5763b7983b3c3c82d2f3174c0ae(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    *,
    auto_enable_controls: typing.Optional[builtins.bool] = None,
    consolidated_findings: typing.Optional[builtins.bool] = None,
    enable_default_standards: typing.Optional[builtins.bool] = None,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a3c7c6540108c38734811d36ebf44cea2082245c0349951fa802fe5d0bf242a(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f533d6913d8b417508c076b8a2f6976f51212d31752f3a38283df8a4aa07140(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    *,
    arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b57d3b22d5b272da8e79438c6b00ec488820202a92c8f03c50479475841f4707(
    scope: _constructs_77d1e7e8.IConstruct,
    id: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
