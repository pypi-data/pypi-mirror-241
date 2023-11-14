# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# DryRun 操作，代表请求将会是成功的，只是多传了 DryRun 参数。
DRYRUNOPERATION = 'DryRunOperation'

# 操作失败。
FAILEDOPERATION = 'FailedOperation'

# 证书已过期，暂不支持下发过期证书。
FAILEDOPERATION_CERTIFICATEHASEXPIRED = 'FailedOperation.CertificateHasExpired'

# 证书不存在。
FAILEDOPERATION_CERTIFICATENOTFOUND = 'FailedOperation.CertificateNotFound'

# 账户余额不足
FAILEDOPERATION_INSUFFICIENTACCOUNTBALANCE = 'FailedOperation.InsufficientAccountBalance'

# 站点状态不正确。
FAILEDOPERATION_INVALIDZONESTATUS = 'FailedOperation.InvalidZoneStatus'

# 操作失败。
FAILEDOPERATION_MODIFYFAILED = 'FailedOperation.ModifyFailed'

# 内部错误。
INTERNALERROR = 'InternalError'

# 后台处理出错。
INTERNALERROR_BACKENDERROR = 'InternalError.BackendError'

# 配置已被锁定，请解除配置锁定之后在重试。
INTERNALERROR_CONFIGLOCKED = 'InternalError.ConfigLocked'

# 数据库错误。
INTERNALERROR_DBERROR = 'InternalError.DBError'

# 获取配置失败。
INTERNALERROR_DOMAINCONFIG = 'InternalError.DomainConfig'

# 上传链接生成失败。
INTERNALERROR_FAILEDTOGENERATEURL = 'InternalError.FailedToGenerateUrl'

# 获取角色失败。
INTERNALERROR_GETROLEERROR = 'InternalError.GetRoleError'

# 后端服务器发生未知错误。
INTERNALERROR_PROXYSERVER = 'InternalError.ProxyServer'

# 配额系统处理失败。
INTERNALERROR_QUOTASYSTEM = 'InternalError.QuotaSystem'

# 后端服务路由地址错误。
INTERNALERROR_ROUTEERROR = 'InternalError.RouteError'

# 内部错误-系统错误。
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# 未知错误。
INTERNALERROR_UNKNOWERROR = 'InternalError.UnknowError'

# 参数错误。
INVALIDPARAMETER = 'InvalidParameter'

# 正则表达式非标准RE2格式。
INVALIDPARAMETER_ACCESSREDIRECTREGEXERROR = 'InvalidParameter.AccessRedirectRegexError'

# 操作频繁，请稍后重试。
INVALIDPARAMETER_ACTIONINPROGRESS = 'InvalidParameter.ActionInProgress'

# 别称域名不支持配置国密证书。
INVALIDPARAMETER_ALIASDOMAINNOTSUPPORTSMCERT = 'InvalidParameter.AliasDomainNotSupportSMCert'

# 无效的查询字符串。
INVALIDPARAMETER_CACHEKEYQUERYSTRINGREQUIRESFULLURLCACHEOFF = 'InvalidParameter.CacheKeyQueryStringRequiresFullUrlCacheOff'

# 查询字符串规则超过了限制。
INVALIDPARAMETER_CACHEKEYQUERYSTRINGTOOMANYVALUE = 'InvalidParameter.CacheKeyQueryStringTooManyValue'

# HTTPS证书和域名不匹配。
INVALIDPARAMETER_CERTNOTMATCHDOMAIN = 'InvalidParameter.CertNotMatchDomain'

# 内部错误。
INVALIDPARAMETER_CERTSYSTEMERROR = 'InvalidParameter.CertSystemError'

# HTTPS证书即将过期。
INVALIDPARAMETER_CERTTOEXPIRE = 'InvalidParameter.CertToExpire'

# 证书错误。
INVALIDPARAMETER_CERTTOOSHORTKEYSIZE = 'InvalidParameter.CertTooShortKeySize'

# IPv6 访问与客户端 IP 地理位置功能冲突。
INVALIDPARAMETER_CLIENTIPCOUNTRYCONFLICTSWITHIPV6 = 'InvalidParameter.ClientIpCountryConflictsWithIpv6'

# CNAME模式下无法申请泛域名证书。
INVALIDPARAMETER_CNAMEWILDHOSTNOTALLOWAPPLYCERTIFICATE = 'InvalidParameter.CnameWildHostNotAllowApplyCertificate'

# 源站不能和域名一致。
INVALIDPARAMETER_CONFLICTHOSTORIGIN = 'InvalidParameter.ConflictHostOrigin'

# 域名不存在或不属于该账号。
INVALIDPARAMETER_DOMAINNOTFOUND = 'InvalidParameter.DomainNotFound'

# 当前域名已开启流量调度功能。
INVALIDPARAMETER_DOMAINONTRAFFICSCHEDULING = 'InvalidParameter.DomainOnTrafficScheduling'

# 操作不支持条件。
INVALIDPARAMETER_ERRACTIONUNSUPPORTTARGET = 'InvalidParameter.ErrActionUnsupportTarget'

# 非法操作。
INVALIDPARAMETER_ERRINVALIDACTION = 'InvalidParameter.ErrInvalidAction'

# 非法操作-操作配置重复。
INVALIDPARAMETER_ERRINVALIDACTIONDUPLICATEACTION = 'InvalidParameter.ErrInvalidActionDuplicateAction'

# 非法操作-非法参数。
INVALIDPARAMETER_ERRINVALIDACTIONPARAM = 'InvalidParameter.ErrInvalidActionParam'

# 非法操作-非法参数-无效action。
INVALIDPARAMETER_ERRINVALIDACTIONPARAMACTION = 'InvalidParameter.ErrInvalidActionParamAction'

# 非法操作-非法参数-无效参数值类型。
INVALIDPARAMETER_ERRINVALIDACTIONPARAMBADVALUETYPE = 'InvalidParameter.ErrInvalidActionParamBadValueType'

# 非法操作-非法参数-参数名重复。
INVALIDPARAMETER_ERRINVALIDACTIONPARAMDUPLICATENAME = 'InvalidParameter.ErrInvalidActionParamDuplicateName'

# 非法操作-非法参数-无效参数值类型。
INVALIDPARAMETER_ERRINVALIDACTIONPARAMNAME = 'InvalidParameter.ErrInvalidActionParamName'

# 非法操作-非法参数-参数值数量超出限制。
INVALIDPARAMETER_ERRINVALIDACTIONPARAMTOOMANYVALUES = 'InvalidParameter.ErrInvalidActionParamTooManyValues'

# 非法操作-非法参数-无效参数值。
INVALIDPARAMETER_ERRINVALIDACTIONPARAMVALUE = 'InvalidParameter.ErrInvalidActionParamValue'

# 非法操作-非法类型。
INVALIDPARAMETER_ERRINVALIDACTIONTYPE = 'InvalidParameter.ErrInvalidActionType'

# 非法条件。
INVALIDPARAMETER_ERRINVALIDCONDITION = 'InvalidParameter.ErrInvalidCondition'

# 修改源站操作仅支持配置一个host匹配类型。
INVALIDPARAMETER_ERRINVALIDCONDITIONHOSTTOOMANYWHENMODIFYORIGINACTIONCONFIGURED = 'InvalidParameter.ErrInvalidConditionHostTooManyWhenModifyOriginActionConfigured'

# 非法条件-非法忽略大小写。
INVALIDPARAMETER_ERRINVALIDCONDITIONIGNORECASE = 'InvalidParameter.ErrInvalidConditionIgnoreCase'

# 非法条件-非法参数名称-无效的参数名称。
INVALIDPARAMETER_ERRINVALIDCONDITIONNAMEBADNAME = 'InvalidParameter.ErrInvalidConditionNameBadName'

# 非法条件-非法参数名称-匹配类型不支持参数名称。
INVALIDPARAMETER_ERRINVALIDCONDITIONNAMETARGETNOTSUPPORTNAME = 'InvalidParameter.ErrInvalidConditionNameTargetNotSupportName'

# 非法条件-非法参数值-无效的正则表达式。
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADREGULAR = 'InvalidParameter.ErrInvalidConditionValueBadRegular'

# 非法条件-非法参数值-无效的url。
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADURL = 'InvalidParameter.ErrInvalidConditionValueBadUrl'

# 非法条件-非法参数值-无效的参数值。
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADVALUE = 'InvalidParameter.ErrInvalidConditionValueBadValue'

# 非法条件-非法参数值-无效的参数值-文件名不应包含文件后缀。
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADVALUECONTAINFILENAMEEXTENSION = 'InvalidParameter.ErrInvalidConditionValueBadValueContainFileNameExtension'

# 非法条件-非法参数值-参数值长度超出限制。
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOLONGVALUE = 'InvalidParameter.ErrInvalidConditionValueTooLongValue'

# 非法条件-非法参数值-正则表达式数量超出限制。
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYREGULAR = 'InvalidParameter.ErrInvalidConditionValueTooManyRegular'

# 非法条件-非法参数值-参数值数量超出限制。
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYVALUES = 'InvalidParameter.ErrInvalidConditionValueTooManyValues'

# 非法条件-非法参数值-通配符数量超出限制。
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYWILDCARD = 'InvalidParameter.ErrInvalidConditionValueTooManyWildcard'

# 非法条件-非法参数值-参数值数量为0。
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEZEROLENGTH = 'InvalidParameter.ErrInvalidConditionValueZeroLength'

# 修改源站操作不支持ELSE。
INVALIDPARAMETER_ERRINVALIDELSEWHENMODIFYORIGINACTIONCONFIGURED = 'InvalidParameter.ErrInvalidElseWhenModifyOriginActionConfigured'

# 条件为空。
INVALIDPARAMETER_ERRNILCONDITION = 'InvalidParameter.ErrNilCondition'

# 开启 Grpc 协议支持需要同时开启 HTTP/2 协议支持。
INVALIDPARAMETER_GRPCREQUIREHTTP2 = 'InvalidParameter.GrpcRequireHttp2'

# 回源Host错误。
INVALIDPARAMETER_HOSTHEADERINVALID = 'InvalidParameter.HostHeaderInvalid'

# 域名不存在。
INVALIDPARAMETER_HOSTNOTFOUND = 'InvalidParameter.HostNotFound'

# CNAME 未切换或者源站未路由到EO服务器。
INVALIDPARAMETER_HOSTSTATUSNOTALLOWAPPLYCERTIFICATE = 'InvalidParameter.HostStatusNotAllowApplyCertificate'

# 参数错误。
INVALIDPARAMETER_INVALIDACCELERATETYPE = 'InvalidParameter.InvalidAccelerateType'

# 无效的token鉴权。
INVALIDPARAMETER_INVALIDAUTHENTICATION = 'InvalidParameter.InvalidAuthentication'

# 无效的token鉴权过期时间。
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPEEXPIRETIME = 'InvalidParameter.InvalidAuthenticationTypeExpireTime'

# 无效的token鉴权密钥。
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESECRETKEY = 'InvalidParameter.InvalidAuthenticationTypeSecretKey'

# 无效的token鉴权参数。
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESIGNPARAM = 'InvalidParameter.InvalidAuthenticationTypeSignParam'

# 无效的token鉴权时间格式。
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPETIMEFORMAT = 'InvalidParameter.InvalidAuthenticationTypeTimeFormat'

# 无效的token鉴权时间参数。
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPETIMEPARAM = 'InvalidParameter.InvalidAuthenticationTypeTimeParam'

# 无效的第三方对象存储。
INVALIDPARAMETER_INVALIDAWSPRIVATEACCESS = 'InvalidParameter.InvalidAwsPrivateAccess'

# 请正确填写地域作为第三方对象存储私有访问参数。
INVALIDPARAMETER_INVALIDAWSREGION = 'InvalidParameter.InvalidAwsRegion'

# 无效的第三方对象存储。
INVALIDPARAMETER_INVALIDAWSSECRETKEY = 'InvalidParameter.InvalidAwsSecretKey'

# 无效的备源回源Host。
INVALIDPARAMETER_INVALIDBACKUPSERVERNAME = 'InvalidParameter.InvalidBackupServerName'

# 无效的节点缓存。
INVALIDPARAMETER_INVALIDCACHECONFIGCACHE = 'InvalidParameter.InvalidCacheConfigCache'

# 无效的节点缓存，遵循源站行为。
INVALIDPARAMETER_INVALIDCACHECONFIGFOLLOWORIGIN = 'InvalidParameter.InvalidCacheConfigFollowOrigin'

# 无效的缓存键。
INVALIDPARAMETER_INVALIDCACHEKEY = 'InvalidParameter.InvalidCacheKey'

# 无效的自定义Cache Key Cookie无效。
INVALIDPARAMETER_INVALIDCACHEKEYCOOKIE = 'InvalidParameter.InvalidCacheKeyCookie'

# 无效的缓存键忽略大小写。
INVALIDPARAMETER_INVALIDCACHEKEYIGNORECASE = 'InvalidParameter.InvalidCacheKeyIgnoreCase'

# 无效的查询字符串。
INVALIDPARAMETER_INVALIDCACHEKEYQUERYSTRINGVALUE = 'InvalidParameter.InvalidCacheKeyQueryStringValue'

# 无效的自定义Cache Key Scheme无效。
INVALIDPARAMETER_INVALIDCACHEKEYSCHEME = 'InvalidParameter.InvalidCacheKeyScheme'

# 无效的节点缓存。
INVALIDPARAMETER_INVALIDCACHEONLYONSWITCH = 'InvalidParameter.InvalidCacheOnlyOnSwitch'

# 无效的节点缓存时间。
INVALIDPARAMETER_INVALIDCACHETIME = 'InvalidParameter.InvalidCacheTime'

# 证书信息错误。
INVALIDPARAMETER_INVALIDCERTINFO = 'InvalidParameter.InvalidCertInfo'

# 无效的客户端IP请求头。
INVALIDPARAMETER_INVALIDCLIENTIPHEADERNAME = 'InvalidParameter.InvalidClientIpHeaderName'

# 分区域回源的源站无效。
INVALIDPARAMETER_INVALIDCLIENTIPORIGIN = 'InvalidParameter.InvalidClientIpOrigin'

# 无效的回源配置，源站类型为对象存储时，源站地址必须为对象存储域名。
INVALIDPARAMETER_INVALIDCOSDOMAIN = 'InvalidParameter.InvalidCosDomain'

# 无效的智能加速。
INVALIDPARAMETER_INVALIDDYNAMICROUTINE = 'InvalidParameter.InvalidDynamicRoutine'

# 套餐包不支持智能加速配置。
INVALIDPARAMETER_INVALIDDYNAMICROUTINEBILLING = 'InvalidParameter.InvalidDynamicRoutineBilling'

# 无效的自定义错误页面。
INVALIDPARAMETER_INVALIDERRORPAGE = 'InvalidParameter.InvalidErrorPage'

# 无效的自定义错误页面。
INVALIDPARAMETER_INVALIDERRORPAGEREDIRECTURL = 'InvalidParameter.InvalidErrorPageRedirectUrl'

# 无效的强制HTTPS跳转。
INVALIDPARAMETER_INVALIDFORCEREDIRECTTYPE = 'InvalidParameter.InvalidForceRedirectType'

# 无效的HTTPS。
INVALIDPARAMETER_INVALIDHTTPS = 'InvalidParameter.InvalidHttps'

# 无效的HTTPS证书。
INVALIDPARAMETER_INVALIDHTTPSCERTINFO = 'InvalidParameter.InvalidHttpsCertInfo'

# 加密套件与TLS版本不匹配。
INVALIDPARAMETER_INVALIDHTTPSCIPHERSUITEANDTLSVERSION = 'InvalidParameter.InvalidHttpsCipherSuiteAndTlsVersion'

# 无效的HTTPS HSTS。
INVALIDPARAMETER_INVALIDHTTPSHSTSMAXAGE = 'InvalidParameter.InvalidHttpsHstsMaxAge'

# 无效的HTTPS TLS版本。
INVALIDPARAMETER_INVALIDHTTPSTLSVERSION = 'InvalidParameter.InvalidHttpsTlsVersion'

# 无效的Ipv6开关配置。
INVALIDPARAMETER_INVALIDIPV6SWITCH = 'InvalidParameter.InvalidIpv6Switch'

# 无效的浏览器缓存。
INVALIDPARAMETER_INVALIDMAXAGETIME = 'InvalidParameter.InvalidMaxAgeTime'

# 无效的源站。
INVALIDPARAMETER_INVALIDORIGIN = 'InvalidParameter.InvalidOrigin'

# 不支持填写内网IP/回环地址作为源站地址
INVALIDPARAMETER_INVALIDORIGINIP = 'InvalidParameter.InvalidOriginIp'

# 参数错误。
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# 套餐包不支持最大上传大小。
INVALIDPARAMETER_INVALIDPOSTMAXSIZEBILLING = 'InvalidParameter.InvalidPostMaxSizeBilling'

# 无效的最大上传大小。
INVALIDPARAMETER_INVALIDPOSTSIZEVALUE = 'InvalidParameter.InvalidPostSizeValue'

# 请填写AccessKeyId、SecretAccessKey作为第三方对象存储私有访问参数。
INVALIDPARAMETER_INVALIDPRIVATEACCESSPARAMS = 'InvalidParameter.InvalidPrivateAccessParams'

# 请指定PrivateAccess参数值为on/off。
INVALIDPARAMETER_INVALIDPRIVATEACCESSSWITCH = 'InvalidParameter.InvalidPrivateAccessSwitch'

# 套餐包不支持Quic配置。
INVALIDPARAMETER_INVALIDQUICBILLING = 'InvalidParameter.InvalidQuicBilling'

# 无效的分片回源。
INVALIDPARAMETER_INVALIDRANGEORIGINPULL = 'InvalidParameter.InvalidRangeOriginPull'

# 无效的请求头header。
INVALIDPARAMETER_INVALIDREQUESTHEADERNAME = 'InvalidParameter.InvalidRequestHeaderName'

# x-forwarded-for 请求头配置无效
INVALIDPARAMETER_INVALIDREQUESTHEADERNAMEXFF = 'InvalidParameter.InvalidRequestHeaderNameXff'

# 无效的请求头header。
INVALIDPARAMETER_INVALIDREQUESTHEADERVALUE = 'InvalidParameter.InvalidRequestHeaderValue'

# 无套餐包。
INVALIDPARAMETER_INVALIDRESOURCEIDBILLING = 'InvalidParameter.InvalidResourceIdBilling'

# 无效的响应头header。
INVALIDPARAMETER_INVALIDRESPONSEHEADERNAME = 'InvalidParameter.InvalidResponseHeaderName'

# 无效的响应头header。
INVALIDPARAMETER_INVALIDRESPONSEHEADERVALUE = 'InvalidParameter.InvalidResponseHeaderValue'

# 无效的规则引擎操作。
INVALIDPARAMETER_INVALIDRULEENGINEACTION = 'InvalidParameter.InvalidRuleEngineAction'

# 规则不存在。
INVALIDPARAMETER_INVALIDRULEENGINENOTFOUND = 'InvalidParameter.InvalidRuleEngineNotFound'

# 无效的规则引擎条件。
INVALIDPARAMETER_INVALIDRULEENGINETARGET = 'InvalidParameter.InvalidRuleEngineTarget'

# 无效的规则引擎文件后缀条件。
INVALIDPARAMETER_INVALIDRULEENGINETARGETSEXTENSION = 'InvalidParameter.InvalidRuleEngineTargetsExtension'

# 无效的规则引擎URL条件。
INVALIDPARAMETER_INVALIDRULEENGINETARGETSURL = 'InvalidParameter.InvalidRuleEngineTargetsUrl'

# 无效的回源Host。
INVALIDPARAMETER_INVALIDSERVERNAME = 'InvalidParameter.InvalidServerName'

# 无效的客户端ip或ip段。
INVALIDPARAMETER_INVALIDSTANDARDDEBUGCLIENTIP = 'InvalidParameter.InvalidStandardDebugClientIp'

# 有效期超过限制。
INVALIDPARAMETER_INVALIDSTANDARDDEBUGEXPIRETIMELIMIT = 'InvalidParameter.InvalidStandardDebugExpireTimeLimit'

# 无效的回源请求参数设置-无效查询字符串值。
INVALIDPARAMETER_INVALIDUPSTREAMREQUESTQUERYSTRINGVALUE = 'InvalidParameter.InvalidUpstreamRequestQueryStringValue'

# 无效的URL重写。
INVALIDPARAMETER_INVALIDURLREDIRECT = 'InvalidParameter.InvalidUrlRedirect'

# URL重写的目标HOST无效。
INVALIDPARAMETER_INVALIDURLREDIRECTHOST = 'InvalidParameter.InvalidUrlRedirectHost'

# URL重写的目标URL无效。
INVALIDPARAMETER_INVALIDURLREDIRECTURL = 'InvalidParameter.InvalidUrlRedirectUrl'

# 无效的WebSocket。
INVALIDPARAMETER_INVALIDWEBSOCKETTIMEOUT = 'InvalidParameter.InvalidWebSocketTimeout'

# 无效的缓存键。
INVALIDPARAMETER_KEYRULESINVALIDQUERYSTRINGVALUE = 'InvalidParameter.KeyRulesInvalidQueryStringValue'

# 参数长度超过限制。
INVALIDPARAMETER_LENGTHEXCEEDSLIMIT = 'InvalidParameter.LengthExceedsLimit'

# 不支持智能路由
INVALIDPARAMETER_MULTIPLYLAYERNOTSUPPORTSMARTROUTING = 'InvalidParameter.MultiplyLayerNotSupportSmartRouting'

# 操作配置存在不支持的预设变量。
INVALIDPARAMETER_NOTSUPPORTTHISPRESET = 'InvalidParameter.NotSupportThisPreset'

# 域名处于直接回源架构，需要保持智能加速功能的开启。
INVALIDPARAMETER_OCDIRECTORIGINREQUIRESSMARTROUTING = 'InvalidParameter.OCDirectOriginRequiresSmartRouting'

# 源站是内网IP。
INVALIDPARAMETER_ORIGINISINNERIP = 'InvalidParameter.OriginIsInnerIp'

# 源站组名称已经存在。
INVALIDPARAMETER_ORIGINNAMEEXISTS = 'InvalidParameter.OriginNameExists'

# 修改源站操作中源站组Id必填。
INVALIDPARAMETER_ORIGINORIGINGROUPIDISREQUIRED = 'InvalidParameter.OriginOriginGroupIdIsRequired'

# 源站格式错误。
INVALIDPARAMETER_ORIGINRECORDFORMATERROR = 'InvalidParameter.OriginRecordFormatError'

# 参数错误: 无效 "结束时间", 不在允许的查询范围内: [开始时间, 开始+ 7天]
INVALIDPARAMETER_PARAMETERERROR = 'InvalidParameter.ParameterError'

# 套餐不存在。
INVALIDPARAMETER_PLANNOTFOUND = 'InvalidParameter.PlanNotFound'

# 最大上传大小超出限制
INVALIDPARAMETER_POSTMAXSIZELIMITEXCEEDED = 'InvalidParameter.PostMaxSizeLimitExceeded'

# 实例名称重复。
INVALIDPARAMETER_PROXYNAMEDUPLICATING = 'InvalidParameter.ProxyNameDuplicating'

# 规则源站信息格式错误。
INVALIDPARAMETER_RULEORIGINFORMATERROR = 'InvalidParameter.RuleOriginFormatError'

# 规则源站不支持多域名。
INVALIDPARAMETER_RULEORIGINMULTIDOMAIN = 'InvalidParameter.RuleOriginMultiDomain'

# 规则源站端口应为整数。
INVALIDPARAMETER_RULEORIGINPORTINTEGER = 'InvalidParameter.RuleOriginPortInteger'

# 规则源站错误。
INVALIDPARAMETER_RULEORIGINVALUEERROR = 'InvalidParameter.RuleOriginValueError'

# 规则端口重复。
INVALIDPARAMETER_RULEPORTDUPLICATING = 'InvalidParameter.RulePortDuplicating'

# 规则端口段错误。
INVALIDPARAMETER_RULEPORTGROUP = 'InvalidParameter.RulePortGroup'

# 规则端口必须为整数。
INVALIDPARAMETER_RULEPORTINTEGER = 'InvalidParameter.RulePortInteger'

# 参数错误
INVALIDPARAMETER_SECURITY = 'InvalidParameter.Security'

# 配置项参数错误。
INVALIDPARAMETER_SETTINGINVALIDPARAM = 'InvalidParameter.SettingInvalidParam'

# Shield Space 未绑定源站，请先绑定源站后重试。
INVALIDPARAMETER_SPACENOTBINDORIGIN = 'InvalidParameter.SpaceNotBindOrigin'

# 资源存在错误。
INVALIDPARAMETER_TARGET = 'InvalidParameter.Target'

# 任务无法生成。
INVALIDPARAMETER_TASKNOTGENERATED = 'InvalidParameter.TaskNotGenerated'

# 内部错误。
INVALIDPARAMETER_TASKSYSTEMERROR = 'InvalidParameter.TaskSystemError'

# 过滤值过多。
INVALIDPARAMETER_TOOMANYFILTERVALUES = 'InvalidParameter.TooManyFilterValues'

# 文件上传链接存在问题。
INVALIDPARAMETER_UPLOADURL = 'InvalidParameter.UploadUrl'

# 站点已被绑定。
INVALIDPARAMETER_ZONEHASBEENBOUND = 'InvalidParameter.ZoneHasBeenBound'

# 站点升级中，暂不支持进行变更操作，请稍后再试。
INVALIDPARAMETER_ZONEISGRAYPUBLISHING = 'InvalidParameter.ZoneIsGrayPublishing'

# 无域名接入站点切换到CNAME接入类型时站点名称必传。
INVALIDPARAMETER_ZONENAMEISREQUIRED = 'InvalidParameter.ZoneNameIsRequired'

# 站点不存在。
INVALIDPARAMETER_ZONENOTFOUND = 'InvalidParameter.ZoneNotFound'

# 参数取值错误。
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# 与已经添加的记录冲突。
INVALIDPARAMETERVALUE_CONFLICTRECORD = 'InvalidParameterValue.ConflictRecord'

# DNS 记录与 DNSSEC 功能冲突。
INVALIDPARAMETERVALUE_CONFLICTWITHDNSSEC = 'InvalidParameterValue.ConflictWithDNSSEC'

# DNS 记录与 NS 记录冲突。
INVALIDPARAMETERVALUE_CONFLICTWITHNSRECORD = 'InvalidParameterValue.ConflictWithNSRecord'

# 主机记录与记录值不能取值相同。
INVALIDPARAMETERVALUE_CONTENTSAMEASNAME = 'InvalidParameterValue.ContentSameAsName'

# 入参中的域名与站点参数不匹配，请更正后重试。
INVALIDPARAMETERVALUE_DOMAINNOTMATCHZONE = 'InvalidParameterValue.DomainNotMatchZone'

# 无效的别称域名后缀（该域名为内部接入域名，暂不支持作为别称域名接入）。
INVALIDPARAMETERVALUE_INVALIDALIASNAMESUFFIX = 'InvalidParameterValue.InvalidAliasNameSuffix'

# DNS 记录内容错误。
INVALIDPARAMETERVALUE_INVALIDDNSCONTENT = 'InvalidParameterValue.InvalidDNSContent'

# DNS 记录名称错误。
INVALIDPARAMETERVALUE_INVALIDDNSNAME = 'InvalidParameterValue.InvalidDNSName'

# 加速域名名称不合法，加速域名应该由数字、英文字母、连词符组成，且连词符不能位于开头和结尾处。
INVALIDPARAMETERVALUE_INVALIDDOMAINNAME = 'InvalidParameterValue.InvalidDomainName'

# 加速域名状态不符合要求。
INVALIDPARAMETERVALUE_INVALIDDOMAINSTATUS = 'InvalidParameterValue.InvalidDomainStatus'

# DNS 代理域名源站错误。
INVALIDPARAMETERVALUE_INVALIDPROXYORIGIN = 'InvalidParameterValue.InvalidProxyOrigin'

# 不支持接入泛域名 CNAME
INVALIDPARAMETERVALUE_NOTALLOWEDWILDCARDSHAREDCNAME = 'InvalidParameterValue.NotAllowedWildcardSharedCNAME'

# 指定的源站组不存在。
INVALIDPARAMETERVALUE_ORIGINGROUPNOTEXISTS = 'InvalidParameterValue.OriginGroupNotExists'

# 请输入合法的共享 CNAME 前缀，最大支持50个字符。
INVALIDPARAMETERVALUE_SHAREDCNAMEPREFIXNOTMATCH = 'InvalidParameterValue.SharedCNAMEPrefixNotMatch'

# 该同名站点标识已被占用，请重新输入。
INVALIDPARAMETERVALUE_ZONESAMEASNAME = 'InvalidParameterValue.ZoneSameAsName'

# 超过配额限制。
LIMITEXCEEDED = 'LimitExceeded'

# 本次提交的资源数超过上限。
LIMITEXCEEDED_BATCHQUOTA = 'LimitExceeded.BatchQuota'

# 当天提交的资源数超过上限。
LIMITEXCEEDED_DAILYQUOTA = 'LimitExceeded.DailyQuota'

# 计费套餐不支持。
LIMITEXCEEDED_PACKNOTALLOW = 'LimitExceeded.PackNotAllow'

# 查询时间范围超出限制。
LIMITEXCEEDED_QUERYTIMELIMITEXCEEDED = 'LimitExceeded.QueryTimeLimitExceeded'

# 单位时间内接口请求频率达到限制。
LIMITEXCEEDED_RATELIMITEXCEEDED = 'LimitExceeded.RateLimitExceeded'

# 超出功能限制。
LIMITEXCEEDED_SECURITY = 'LimitExceeded.Security'

# 套餐可绑定的站点数量超过配额。
LIMITEXCEEDED_ZONEBINDPLAN = 'LimitExceeded.ZoneBindPlan'

# 操作被拒绝。
OPERATIONDENIED = 'OperationDenied'

# 功能内测中，请联系商务开启「中国大陆网络优化(国际加速)」功能。
OPERATIONDENIED_ACCELERATEMAINLANDDISABLE = 'OperationDenied.AccelerateMainlandDisable'

# 中国大陆加速与IPv6冲突，不能同时配置。
OPERATIONDENIED_ACCELERATEMAINLANDIPV6CONFLICT = 'OperationDenied.AccelerateMainlandIpv6Conflict'

# 引用源站组的7层域名服务正在部署中，请稍后再编辑。
OPERATIONDENIED_ACCELERATIONDOMAINSTATUSNOTINONLINE = 'OperationDenied.AccelerationDomainStatusNotInOnline'

# 配置已被锁定，请解除配置锁定之后在重试。
OPERATIONDENIED_CONFIGLOCKED = 'OperationDenied.ConfigLocked'

# 站点停用未完毕，请稍后再试。
OPERATIONDENIED_DISABLEZONENOTCOMPLETED = 'OperationDenied.DisableZoneNotCompleted'

# 有域名在共享cname组内，不可切换接入类型。
OPERATIONDENIED_DOMAININSHARECNAMEGROUP = 'OperationDenied.DomainInShareCnameGroup'

# 域名被封禁，暂时无法操作。
OPERATIONDENIED_DOMAINISBLOCKED = 'OperationDenied.DomainIsBlocked'

# 域名尚未备案。
OPERATIONDENIED_DOMAINNOICP = 'OperationDenied.DomainNoICP'

# 站点下有域名时不允许修改服务区域。
OPERATIONDENIED_DOMAINNUMBERISNOTZERO = 'OperationDenied.DomainNumberIsNotZero'

# 站点处于停用状态，请开启后重试。
OPERATIONDENIED_ERRZONEISALREADYPAUSED = 'OperationDenied.ErrZoneIsAlreadyPaused'

# 开启高防时必须保证安全是开启状态。
OPERATIONDENIED_INVALIDADVANCEDDEFENSESECURITYTYPE = 'OperationDenied.InvalidAdvancedDefenseSecurityType'

# 开启高防必须保证站点加速区域是国内。
OPERATIONDENIED_INVALIDADVANCEDDEFENSEZONEAREA = 'OperationDenied.InvalidAdvancedDefenseZoneArea'

# 4层代理资源处于封禁中，禁止操作。
OPERATIONDENIED_L4PROXYINBANNEDSTATUS = 'OperationDenied.L4ProxyInBannedStatus'

# 存在四层代理实例处于部署中状态，暂不支持停用站点。
OPERATIONDENIED_L4PROXYINPROGRESSSTATUS = 'OperationDenied.L4ProxyInProgressStatus'

# 存在四层代理实例处于停用中状态，暂不支持停用站点。
OPERATIONDENIED_L4PROXYINSTOPPINGSTATUS = 'OperationDenied.L4ProxyInStoppingStatus'

# 绑定4层实例有处于非运行中的状态，禁止操作。
OPERATIONDENIED_L4STATUSNOTINONLINE = 'OperationDenied.L4StatusNotInOnline'

# 存在加速域名处于部署中状态，暂不支持停用站点。
OPERATIONDENIED_L7HOSTINPROCESSSTATUS = 'OperationDenied.L7HostInProcessStatus'

# 站点状态不支持操作负载均衡。
OPERATIONDENIED_LOADBALANCINGZONEISNOTACTIVE = 'OperationDenied.LoadBalancingZoneIsNotActive'

# 已存在多个Cname接入站点，不允许切换至NS。
OPERATIONDENIED_MULTIPLECNAMEZONE = 'OperationDenied.MultipleCnameZone'

# NS接入模式不支持域名流量调度功能。
OPERATIONDENIED_NSNOTALLOWTRAFFICSTRATEGY = 'OperationDenied.NSNotAllowTrafficStrategy'

# 无域名接入站点仅可以切换到CNAME接入类型。
OPERATIONDENIED_NODOMAINACCESSZONEONLYALLOWMODIFIEDTOCNAME = 'OperationDenied.NoDomainAccessZoneOnlyAllowModifiedToCNAME'

# 无域名接入站点不支持除切换为CNAME接入类型以外的任何修改动作。
OPERATIONDENIED_NODOMAINACCESSZONEONLYSUPPORTMODIFYTYPE = 'OperationDenied.NoDomainAccessZoneOnlySupportModifyType'

# 加速域名使用中，无法删除。
OPERATIONDENIED_ORIGINGROUPACCELERATIONDOMAINUSED = 'OperationDenied.OriginGroupAccelerationDomainUsed'

# 套餐不支持变更站点的服务区域。
OPERATIONDENIED_PLANNOTSUPPORTMODIFYZONEAREA = 'OperationDenied.PlanNotSupportModifyZoneArea'

# Anycast IP调度模式不支持开启中国大陆加速。
OPERATIONDENIED_PLATTYPEIPACCELERATEMAINLANDNOTSUPPORT = 'OperationDenied.PlatTypeIPAccelerateMainlandNotSupport'

# DNS 记录不允许添加。
OPERATIONDENIED_RECORDISFORBIDDEN = 'OperationDenied.RecordIsForbidden'

# 当前有互相排斥的请求操作并行发起，请稍后重试。
OPERATIONDENIED_RESOURCELOCKEDTEMPORARY = 'OperationDenied.ResourceLockedTemporary'

# 绑定在共享 CNAME 中的域名不允许变更 中国大陆网络优化（国际加速）访问，如果您需要单独变更，请先将域名从共享 CNAME 中解绑。
OPERATIONDENIED_SHAREDCNAMEUNSUPPORTEDACCELERATEMAINLAND = 'OperationDenied.SharedCNAMEUnsupportedAccelerateMainland'

# 绑定在共享 CNAME 中的域名不允许变更 IPv6 访问，如果您需要单独变更，请先将域名从共享 CNAME 中解绑。
OPERATIONDENIED_SHAREDCNAMEUNSUPPORTEDIPV6 = 'OperationDenied.SharedCNAMEUnsupportedIPv6'

# 存在使用中的测试版本，请将测试版本发布现网或者回滚测试版本再重试。
OPERATIONDENIED_VERSIONCONTROLISGRAYING = 'OperationDenied.VersionControlIsGraying'

# 共享CNAME已被其他站点绑定，请先解绑才能删除站点
OPERATIONDENIED_ZONEISBINDINGSHAREDCNAME = 'OperationDenied.ZoneIsBindingSharedCNAME'

# 站点存在自定义错误页面引用，请先解绑。
OPERATIONDENIED_ZONEISREFERENCECUSTOMERRORPAGE = 'OperationDenied.ZoneIsReferenceCustomErrorPage'

# 资源被占用。
RESOURCEINUSE = 'ResourceInUse'

# 资源被本账号别称域名占用。
RESOURCEINUSE_ALIASDOMAIN = 'ResourceInUse.AliasDomain'

# 当前已存在相同的别称域名，不支持重复添加
RESOURCEINUSE_ALIASNAME = 'ResourceInUse.AliasName'

# 资源被本账号Cname接入占用。
RESOURCEINUSE_CNAME = 'ResourceInUse.Cname'

# Dns资源被占用。
RESOURCEINUSE_DNS = 'ResourceInUse.Dns'

# 该域名正在解析中，如果您需要开启加速，请前往 DNS 记录页开启加速。
RESOURCEINUSE_DNSRECORD = 'ResourceInUse.DnsRecord'

# 已存在相同的别称域名。
RESOURCEINUSE_DUPLICATENAME = 'ResourceInUse.DuplicateName'

# 资源已被泛域名占用。
RESOURCEINUSE_GENERICHOST = 'ResourceInUse.GenericHost'

# 资源被本账号的子域名占用。
RESOURCEINUSE_HOST = 'ResourceInUse.Host'

# 资源被本账号NS接入占用。
RESOURCEINUSE_NS = 'ResourceInUse.NS'

# 资源被其他用户接入。
RESOURCEINUSE_OTHERS = 'ResourceInUse.Others'

# 资源被其他账号别称域名占用。
RESOURCEINUSE_OTHERSALIASDOMAIN = 'ResourceInUse.OthersAliasDomain'

# 资源被其他账号Cname接入占用。
RESOURCEINUSE_OTHERSCNAME = 'ResourceInUse.OthersCname'

# 资源被其他账号的子域名占用。
RESOURCEINUSE_OTHERSHOST = 'ResourceInUse.OthersHost'

# 资源被其他账号NS接入占用。
RESOURCEINUSE_OTHERSNS = 'ResourceInUse.OthersNS'

# 资源被本账号和其他账号同时Cname接入占用。
RESOURCEINUSE_SELFANDOTHERSCNAME = 'ResourceInUse.SelfAndOthersCname'

# 该共享 CNAME 已绑定加速域名，禁止删除。如您需要删除，请先将对应域名解绑。
RESOURCEINUSE_SHAREDCNAME = 'ResourceInUse.SharedCNAME'

# 别称域名已站点接入。
RESOURCEINUSE_ZONE = 'ResourceInUse.Zone'

# 资源不足。
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# 资源不存在。
RESOURCENOTFOUND = 'ResourceNotFound'

# 最大上传大小额度未配置
RESOURCENOTFOUND_POSTMAXSIZEQUOTANOTFOUND = 'ResourceNotFound.PostMaxSizeQuotaNotFound'

# 资源不可用。
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# 证书不存在或未授权。
RESOURCEUNAVAILABLE_CERTNOTFOUND = 'ResourceUnavailable.CertNotFound'

# 当前域名已接入EdgeOne，如确认需要接入到当前账号，请进行域名找回。
RESOURCEUNAVAILABLE_DOMAINALREADYEXISTS = 'ResourceUnavailable.DomainAlreadyExists'

# 请求的加速域名不存在，请更正后重试。
RESOURCEUNAVAILABLE_DOMAINNOTFOUND = 'ResourceUnavailable.DomainNotFound'

# 域名不存在或未开启代理。
RESOURCEUNAVAILABLE_HOSTNOTFOUND = 'ResourceUnavailable.HostNotFound'

# 该共享 CNAME 已被占用，请重新输入。
RESOURCEUNAVAILABLE_SHAREDCNAMEALREADYEXISTS = 'ResourceUnavailable.SharedCNAMEAlreadyExists'

# 站点不存在或不属于该账号。
RESOURCEUNAVAILABLE_ZONENOTFOUND = 'ResourceUnavailable.ZoneNotFound'

# 资源售卖火爆，已售罄，正在加紧补货中，当前无法新增域名，请您耐心等待。
RESOURCESSOLDOUT_L7LACKOFRESOURCES = 'ResourcesSoldOut.L7LackOfResources'

# 未授权操作。
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Cam 未授权。
UNAUTHORIZEDOPERATION_CAMUNAUTHORIZED = 'UnauthorizedOperation.CamUnauthorized'

# 鉴权错误。
UNAUTHORIZEDOPERATION_DOMAINEMPTY = 'UnauthorizedOperation.DomainEmpty'

# 子账户没有操作权限，请添加权限后继续操作。
UNAUTHORIZEDOPERATION_NOPERMISSION = 'UnauthorizedOperation.NoPermission'

# 后端服务器发生未知错误。
UNAUTHORIZEDOPERATION_UNKNOWN = 'UnauthorizedOperation.Unknown'

# 操作不支持。
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# 别称域名不支持目标域名源站类型为对象存储。
UNSUPPORTEDOPERATION_TARGETNAMEORIGINTYPECOS = 'UnsupportedOperation.TargetNameOriginTypeCos'
