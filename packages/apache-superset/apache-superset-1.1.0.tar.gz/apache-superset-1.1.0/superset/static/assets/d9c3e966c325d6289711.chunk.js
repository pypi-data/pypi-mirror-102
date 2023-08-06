(window.webpackJsonp=window.webpackJsonp||[]).push([[18],{153:function(e,t,a){"use strict";const l=a(22).q;t.a=l},205:function(e,t,a){"use strict";a.d(t,"a",(function(){return c})),a.d(t,"b",(function(){return i})),a.d(t,"c",(function(){return r}));a(261);var l=a(8),n=a.n(l);const c=" : ",i=(e,t)=>`${e}${c}${t}`,o=(e,t)=>e.replace("T00:00:00","")||(t?"-∞":"∞"),r=(e,t)=>{var a;const l=e.split(c);if(1===l.length)return e;const i=n()(a=t||["unknown","unknown"]).call(a,e=>"inclusive"===e?"≤":"<");return`${o(l[0],!0)} ${i[0]} col ${i[1]} ${o(l[1])}`}},983:function(e,t,a){"use strict";a.d(t,"a",(function(){return Me}));a(38);var l=a(32),n=a.n(l),c=a(0),i=a.n(c),o=a(98),r=a.n(o),u=a(71),s=a(50),b=a(14),d=a(205),f=a(67),O=a(37),j=a(83),m=a(107),h=a(153),v=a(22),p=a(47),g=a(77),y=a(51),w=a(44),$=a.n(w),C=a(8),D=a.n(C),E=a(70),x=a.n(E),N=a(28),T=a.n(N);const A=[{value:"Common",label:Object(b.e)("Last")},{value:"Calendar",label:Object(b.e)("Previous")},{value:"Custom",label:Object(b.e)("Custom")},{value:"Advanced",label:Object(b.e)("Advanced")},{value:"No filter",label:Object(b.e)("No filter")}],M=[{value:"Last day",label:Object(b.e)("last day")},{value:"Last week",label:Object(b.e)("last week")},{value:"Last month",label:Object(b.e)("last month")},{value:"Last quarter",label:Object(b.e)("last quarter")},{value:"Last year",label:Object(b.e)("last year")}],k=new x.a(D()(M).call(M,({value:e})=>e)),S=[{value:"previous calendar week",label:Object(b.e)("previous calendar week")},{value:"previous calendar month",label:Object(b.e)("previous calendar month")},{value:"previous calendar year",label:Object(b.e)("previous calendar year")}],G=new x.a(D()(S).call(S,({value:e})=>e)),V=[{value:"second",label:e=>`${Object(b.e)("Seconds")} ${e}`},{value:"minute",label:e=>`${Object(b.e)("Minutes")} ${e}`},{value:"hour",label:e=>`${Object(b.e)("Hours")} ${e}`},{value:"day",label:e=>`${Object(b.e)("Days")} ${e}`},{value:"week",label:e=>`${Object(b.e)("Weeks")} ${e}`},{value:"month",label:e=>`${Object(b.e)("Months")} ${e}`},{value:"quarter",label:e=>`${Object(b.e)("Quarters")} ${e}`},{value:"year",label:e=>`${Object(b.e)("Years")} ${e}`}],L=D()(V).call(V,e=>({value:e.value,label:e.label(Object(b.e)("Before"))})),R=D()(V).call(V,e=>({value:e.value,label:e.label(Object(b.e)("After"))})),I=[{value:"specific",label:Object(b.e)("Specific Date/Time")},{value:"relative",label:Object(b.e)("Relative Date/Time")},{value:"now",label:Object(b.e)("Now")},{value:"today",label:Object(b.e)("Midnight")}],F=$()(I).call(I),U=new x.a(["Last day","Last week","Last month","Last quarter","Last year"]),Y=new x.a(["previous calendar week","previous calendar month","previous calendar year"]),q="YYYY-MM-DD[T]HH:mm:ss",z=T()().utc().startOf("day").subtract(7,"days").format(q),H=T()().utc().startOf("day").format(q);var P=a(133),W=a.n(P),B=a(33),J=a.n(B),K=a(552),Q=a.n(K);const X=Q.a`\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:(?:[+-]\d\d:\d\d)|Z)?`,Z=Q.a`TODAY|NOW`,_=Q.a`[+-]?[1-9][0-9]*`,ee=Q.a`YEAR|QUARTER|MONTH|WEEK|DAY|HOUR|MINUTE|SECOND`,te=RegExp(Q.a`^DATEADD\(DATETIME\("(${X}|${Z})"\),\s(${_}),\s(${ee})\)$`,"i"),ae=RegExp(Q.a`^${X}$|^${Z}$`,"i"),le=["now","today"],ne={sinceDatetime:z,sinceMode:"relative",sinceGrain:"day",sinceGrainValue:-7,untilDatetime:H,untilMode:"specific",untilGrain:"day",untilGrainValue:7,anchorMode:"now",anchorValue:"now"},ce=["specific","today","now"],ie=e=>"now"===e?T()().utc().startOf("second"):"today"===e?T()().utc().startOf("day"):T()(e),oe=e=>ie(e).format(q),re=e=>{const t=e.split(d.a);if(2===t.length){const[e,a]=t;if(ae.test(e)&&ae.test(a)){const t=J()(le).call(le,e)?e:"specific",l=J()(le).call(le,a)?a:"specific";return{customRange:{...ne,sinceDatetime:e,untilDatetime:a,sinceMode:t,untilMode:l},matchedFlag:!0}}const l=e.match(te);if(l&&ae.test(a)&&J()(e).call(e,a)){const[e,t,n]=$()(l).call(l,1),c=J()(le).call(le,a)?a:"specific";return{customRange:{...ne,sinceGrain:n,sinceGrainValue:W()(t,10),sinceDatetime:e,untilDatetime:e,sinceMode:"relative",untilMode:c},matchedFlag:!0}}const n=a.match(te);if(ae.test(e)&&n&&J()(a).call(a,e)){const[t,a,l]=[...$()(n).call(n,1)],c=J()(le).call(le,e)?e:"specific";return{customRange:{...ne,untilGrain:l,untilGrainValue:W()(a,10),sinceDatetime:t,untilDatetime:t,untilMode:"relative",sinceMode:c},matchedFlag:!0}}if(l&&n){const[e,t,a]=[...$()(l).call(l,1)],[c,i,o]=[...$()(n).call(n,1)];if(e===c)return{customRange:{...ne,sinceGrain:a,sinceGrainValue:W()(t,10),sinceDatetime:e,untilGrain:o,untilGrainValue:W()(i,10),untilDatetime:c,anchorValue:e,sinceMode:"relative",untilMode:"relative",anchorMode:"now"===e?"now":"specific"},matchedFlag:!0}}}return{customRange:ne,matchedFlag:!1}},ue=e=>{const{sinceDatetime:t,sinceMode:a,sinceGrain:l,sinceGrainValue:n,untilDatetime:c,untilMode:i,untilGrain:o,untilGrainValue:r,anchorValue:u}={...e};if(J()(ce).call(ce,a)&&J()(ce).call(ce,i)){return`${"specific"===a?oe(t):a} : ${"specific"===i?oe(c):i}`}if(J()(ce).call(ce,a)&&"relative"===i){const e="specific"===a?oe(t):a;return`${e} : ${`DATEADD(DATETIME("${e}"), ${r}, ${o})`}`}if("relative"===a&&J()(ce).call(ce,i)){const e="specific"===i?oe(c):i;return`${`DATEADD(DATETIME("${e}"), ${-Math.abs(n)}, ${l})`} : ${e}`}return`${`DATEADD(DATETIME("${u}"), ${-Math.abs(n)}, ${l})`} : ${`DATEADD(DATETIME("${u}"), ${r}, ${o})`}`};var se=a(167),be=a(1);function de(e){let t="Last week";return U.has(e.value)?t=e.value:e.onChange(t),Object(be.f)(i.a.Fragment,null,Object(be.f)("div",{className:"section-title"},Object(b.e)("Configure Time Range: Last...")),Object(be.f)(se.a.Group,{value:t,onChange:t=>e.onChange(t.target.value)},D()(M).call(M,({value:e,label:t})=>Object(be.f)(se.a,{key:e,value:e,className:"vertical-radio"},t))))}function fe(e){let t="previous calendar week";return Y.has(e.value)?t=e.value:e.onChange(t),Object(be.f)(i.a.Fragment,null,Object(be.f)("div",{className:"section-title"},Object(b.e)("Configure Time Range: Previous...")),Object(be.f)(se.a.Group,{value:t,onChange:t=>e.onChange(t.target.value)},D()(S).call(S,({value:e,label:t})=>Object(be.f)(se.a,{key:e,value:e,className:"vertical-radio"},t))))}var Oe=a(1155),je=a.n(Oe),me=a(112);function he(e){const{customRange:t,matchedFlag:a}=re(e.value);a||e.onChange(ue(t));const{sinceDatetime:l,sinceMode:c,sinceGrain:i,sinceGrainValue:o,untilDatetime:r,untilMode:u,untilGrain:s,untilGrainValue:d,anchorValue:f,anchorMode:O}={...t};function j(a,l){e.onChange(ue({...t,[a]:l}))}function m(a,l){je()(l)&&l>0&&e.onChange(ue({...t,[a]:l}))}return Object(be.f)("div",null,Object(be.f)("div",{className:"section-title"},Object(b.e)("Configure custom time range")),Object(be.f)(v.r,{gutter:24},Object(be.f)(v.f,{span:12},Object(be.f)("div",{className:"control-label"},Object(b.e)("START (INCLUSIVE)")," ",Object(be.f)(me.a,{tooltip:Object(b.e)("Start date included in time range"),placement:"right"})),Object(be.f)(g.f,{options:I,value:n()(I).call(I,e=>e.value===c),onChange:e=>j("sinceMode",e.value)}),"specific"===c&&Object(be.f)(v.r,null,Object(be.f)(v.g,{showTime:!0,value:ie(l),onSelect:e=>j("sinceDatetime",e.format(q)),allowClear:!1})),"relative"===c&&Object(be.f)(v.r,{gutter:8},Object(be.f)(v.f,{span:11},Object(be.f)(v.m,{placeholder:Object(b.e)("Relative quantity"),value:Math.abs(o),min:1,defaultValue:1,onChange:e=>m("sinceGrainValue",e||1),onStep:e=>m("sinceGrainValue",e||1)})),Object(be.f)(v.f,{span:13},Object(be.f)(g.f,{options:L,value:n()(L).call(L,e=>e.value===i),onChange:e=>j("sinceGrain",e.value)})))),Object(be.f)(v.f,{span:12},Object(be.f)("div",{className:"control-label"},Object(b.e)("END (EXCLUSIVE)")," ",Object(be.f)(me.a,{tooltip:Object(b.e)("End date excluded from time range"),placement:"right"})),Object(be.f)(g.f,{options:F,value:n()(F).call(F,e=>e.value===u),onChange:e=>j("untilMode",e.value)}),"specific"===u&&Object(be.f)(v.r,null,Object(be.f)(v.g,{showTime:!0,value:ie(r),onSelect:e=>j("untilDatetime",e.format(q)),allowClear:!1})),"relative"===u&&Object(be.f)(v.r,{gutter:8},Object(be.f)(v.f,{span:11},Object(be.f)(v.m,{placeholder:Object(b.e)("Relative quantity"),value:d,min:1,defaultValue:1,onChange:e=>m("untilGrainValue",e||1),onStep:e=>m("untilGrainValue",e||1)})),Object(be.f)(v.f,{span:13},Object(be.f)(g.f,{options:R,value:n()(R).call(R,e=>e.value===s),onChange:e=>j("untilGrain",e.value)}))))),"relative"===c&&"relative"===u&&Object(be.f)("div",{className:"control-anchor-to"},Object(be.f)("div",{className:"control-label"},Object(b.e)("Anchor to")),Object(be.f)(v.r,{align:"middle"},Object(be.f)(v.f,null,Object(be.f)(se.a.Group,{onChange:function(a){const l=a.target.value;"now"===l?e.onChange(ue({...t,anchorValue:"now",anchorMode:l})):e.onChange(ue({...t,anchorValue:H,anchorMode:l}))},defaultValue:"now",value:O},Object(be.f)(se.a,{key:"now",value:"now"},Object(b.e)("NOW")),Object(be.f)(se.a,{key:"specific",value:"specific"},Object(b.e)("Date/Time")))),"now"!==O&&Object(be.f)(v.f,null,Object(be.f)(v.g,{showTime:!0,value:ie(f),onSelect:e=>j("anchorValue",e.format(q)),allowClear:!1,className:"control-anchor-to-datetime"})))))}var ve=a(231),pe=a.n(ve),ge=a(31),ye=a.n(ge);const we=Object(be.f)(i.a.Fragment,null,Object(be.f)("div",null,Object(be.f)("h3",null,"DATETIME"),Object(be.f)("p",null,Object(b.e)("Return to specific datetime.")),Object(be.f)("h4",null,Object(b.e)("Syntax")),Object(be.f)("pre",null,Object(be.f)("code",null,"datetime([string])")),Object(be.f)("h4",null,Object(b.e)("Example")),Object(be.f)("pre",null,Object(be.f)("code",null,'datetime("2020-03-01 12:00:00")\ndatetime("now")\ndatetime("last year")'))),Object(be.f)("div",null,Object(be.f)("h3",null,"DATEADD"),Object(be.f)("p",null,Object(b.e)("Moves the given set of dates by a specified interval.")),Object(be.f)("h4",null,Object(b.e)("Syntax")),Object(be.f)("pre",null,Object(be.f)("code",null,"dateadd([datetime], [integer], [dateunit])\ndateunit = (year | quarter | month | week | day | hour | minute | second)")),Object(be.f)("h4",null,Object(b.e)("Example")),Object(be.f)("pre",null,Object(be.f)("code",null,'dateadd(datetime("today"), -13, day)\ndateadd(datetime("2020-03-01"), 2, day)'))),Object(be.f)("div",null,Object(be.f)("h3",null,"DATETRUNC"),Object(be.f)("p",null,Object(b.e)("Truncates the specified date to the accuracy specified by the date unit.")),Object(be.f)("h4",null,Object(b.e)("Syntax")),Object(be.f)("pre",null,Object(be.f)("code",null,"datetrunc([datetime], [dateunit])\ndateunit = (year | month | week)")),Object(be.f)("h4",null,Object(b.e)("Example")),Object(be.f)("pre",null,Object(be.f)("code",null,'datetrunc(datetime("2020-03-01"), week)\ndatetrunc(datetime("2020-03-01"), month)'))),Object(be.f)("div",null,Object(be.f)("h3",null,"LASTDAY"),Object(be.f)("p",null,Object(b.e)("Get the last date by the date unit.")),Object(be.f)("h4",null,Object(b.e)("Syntax")),Object(be.f)("pre",null,Object(be.f)("code",null,"lastday([datetime], [dateunit])\ndateunit = (year | month | week)")),Object(be.f)("h4",null,Object(b.e)("Example")),Object(be.f)("pre",null,Object(be.f)("code",null,'lastday(datetime("today"), month)'))),Object(be.f)("div",null,Object(be.f)("h3",null,"HOLIDAY"),Object(be.f)("p",null,Object(b.e)("Get the specify date for the holiday")),Object(be.f)("h4",null,Object(b.e)("Syntax")),Object(be.f)("pre",null,Object(be.f)("code",null,"holiday([string])\nholiday([holiday string], [datetime])\nholiday([holiday string], [datetime], [country name])")),Object(be.f)("h4",null,Object(b.e)("Example")),Object(be.f)("pre",null,Object(be.f)("code",null,'holiday("new year")\nholiday("christmas", datetime("2019"))\nholiday("christmas", dateadd(datetime("2019"), 1, year))\nholiday("christmas", datetime("2 years ago"))\nholiday("Easter Monday", datetime("2019"), "UK")')))),$e=e=>{const t=Object(s.e)();return Object(be.f)(be.b,null,({css:a})=>Object(be.f)(y.a,ye()({overlayClassName:a`
            .ant-tooltip-content {
              min-width: ${125*t.gridUnit}px;
              max-height: 410px;
              overflow-y: scroll;

              .ant-tooltip-inner {
                max-width: ${125*t.gridUnit}px;
                h3 {
                  font-size: ${t.typography.sizes.m}px;
                  font-weight: ${t.typography.weights.bold};
                }
                h4 {
                  font-size: ${t.typography.sizes.m}px;
                  font-weight: ${t.typography.weights.bold};
                }
                pre {
                  border: none;
                  text-align: left;
                  word-break: break-word;
                  font-size: ${t.typography.sizes.s}px;
                }
              }
            }
          `},e)))};function Ce(e){return Object(be.f)($e,ye()({title:we},e))}function De(e){const t=n(e.value||""),[a,l]=t.split(d.a);function n(e){return J()(e).call(e,d.a)?e:pe()(e).call(e,"Last")?[e,""].join(d.a):pe()(e).call(e,"Next")?["",e].join(d.a):d.a}function c(t,n){"since"===t?e.onChange(`${n}${d.a}${l}`):e.onChange(`${a}${d.a}${n}`)}return t!==e.value&&e.onChange(n(e.value||"")),Object(be.f)(i.a.Fragment,null,Object(be.f)("div",{className:"section-title"},Object(b.e)("Configure Advanced Time Range "),Object(be.f)(Ce,{placement:"rightBottom"},Object(be.f)("i",{className:"fa fa-info-circle text-muted"}))),Object(be.f)("div",{className:"control-label"},Object(b.e)("START (INCLUSIVE)")," ",Object(be.f)(me.a,{tooltip:Object(b.e)("Start date included in time range"),placement:"right"})),Object(be.f)(v.l,{key:"since",value:a,onChange:e=>c("since",e.target.value)}),Object(be.f)("div",{className:"control-label"},Object(b.e)("END (EXCLUSIVE)")," ",Object(be.f)(me.a,{tooltip:Object(b.e)("End date excluded from time range"),placement:"right"})),Object(be.f)(v.l,{key:"until",value:l,onChange:e=>c("until",e.target.value)}))}const Ee=e=>k.has(e)?"Common":G.has(e)?"Calendar":"No filter"===e?"No filter":re(e).matchedFlag?"Custom":"Advanced",xe=async(e,t)=>{const a=`/api/v1/time_range/?q=${r.a.encode(e)}`;try{var l,n,c,i;const e=await u.a.get({endpoint:a}),o=Object(d.b)((null==e?void 0:null==(l=e.json)?void 0:null==(n=l.result)?void 0:n.since)||"",(null==e?void 0:null==(c=e.json)?void 0:null==(i=c.result)?void 0:i.until)||"");return{value:Object(d.c)(o,t)}}catch(e){const t=await Object(f.a)(e);return{error:t.message||t.error}}},Ne=Object(s.c)(h.a)``,Te=s.c.div`
  .ant-row {
    margin-top: 8px;
  }

  .ant-input-number {
    width: 100%;
  }

  .frame-dropdown {
    width: 272px;
  }

  .ant-picker {
    padding: 4px 17px 4px;
    border-radius: 4px;
    width: 100%;
  }

  .ant-divider-horizontal {
    margin: 16px 0;
  }

  .control-label {
    font-size: 11px;
    font-weight: 500;
    color: #b2b2b2;
    line-height: 16px;
    text-transform: uppercase;
    margin: 8px 0;
  }

  .vertical-radio {
    display: block;
    height: 40px;
    line-height: 40px;
  }

  .section-title {
    font-style: normal;
    font-weight: 500;
    font-size: 15px;
    line-height: 24px;
    margin-bottom: 8px;
  }

  .control-anchor-to {
    margin-top: 16px;
  }

  .control-anchor-to-datetime {
    width: 217px;
  }

  .footer {
    text-align: right;
  }
`,Ae=s.c.span`
  svg {
    margin-right: ${({theme:e})=>2*e.gridUnit}px;
    vertical-align: middle;
  }
  .text {
    vertical-align: middle;
  }
  .error {
    color: ${({theme:e})=>e.colors.error.base};
  }
`;function Me(e){const{value:t="Last week",endpoints:a,onChange:l,datasource:o}=e,[r,u]=Object(c.useState)(t),[d,f]=Object(c.useState)(!1),[h,w]=Object(c.useState)(Ee(t)),[$,C]=Object(c.useState)(!1),[D,E]=Object(c.useState)(t),[x,N]=Object(c.useState)(!1),[T,M]=Object(c.useState)(t),[k,S]=Object(c.useState)(t);function G(){E(t),w(Ee(t)),f(!1)}Object(c.useEffect)(()=>{$||C(!0),xe(t,a).then(({value:e,error:a})=>{a?(M(a||""),N(!1),S(t||"")):("Common"===h||"Calendar"===h||"No filter"===h?(u(t),S(e||"")):(u(e||""),S(t||"")),N(!0))})},[t]),Object(c.useEffect)(()=>{$&&(l("Last week"),E("Last week"),w(Ee("Last week")))},[o]),Object(c.useEffect)(()=>{xe(D,a).then(({value:e,error:t})=>{t?(M(t||""),N(!1)):(M(e||""),N(!0))})},[D]);const V=Object(be.f)(Te,null,Object(be.f)("div",{className:"control-label"},Object(b.e)("RANGE TYPE")),Object(be.f)(g.f,{options:A,value:n()(A).call(A,({value:e})=>e===h),onChange:function(e){"No filter"===e.value&&E("No filter"),w(e.value)},className:"frame-dropdown"}),"No filter"!==h&&Object(be.f)(v.h,null),"Common"===h&&Object(be.f)(de,{value:D,onChange:E}),"Calendar"===h&&Object(be.f)(fe,{value:D,onChange:E}),"Advanced"===h&&Object(be.f)(De,{value:D,onChange:E}),"Custom"===h&&Object(be.f)(he,{value:D,onChange:E}),"No filter"===h&&Object(be.f)("div",null),Object(be.f)(v.h,null),Object(be.f)("div",null,Object(be.f)("div",{className:"section-title"},Object(b.e)("Actual time range")),x&&Object(be.f)("div",null,T),!x&&Object(be.f)(Ae,{className:"warning"},Object(be.f)(p.a,{name:"error-solid-small",color:s.d.colors.error.base}),Object(be.f)("span",{className:"text error"},T))),Object(be.f)(v.h,null),Object(be.f)("div",{className:"footer"},Object(be.f)(O.a,{buttonStyle:"secondary",cta:!0,key:"cancel",onClick:G},Object(b.e)("CANCEL")),Object(be.f)(O.a,{buttonStyle:"primary",cta:!0,disabled:!x,key:"apply",onClick:function(){l(D),f(!1)}},Object(b.e)("APPLY")))),L=Object(be.f)(Ae,null,Object(be.f)(p.a,{name:"edit-alt"}),Object(be.f)("span",{className:"text"},Object(b.e)("Edit time range")));return Object(be.f)(i.a.Fragment,null,Object(be.f)(j.a,e),Object(be.f)(Ne,{placement:"right",trigger:"click",content:V,title:L,defaultVisible:d,visible:d,onVisibleChange:()=>{d?G():f(!0)},overlayStyle:{width:"600px"}},Object(be.f)(y.a,{placement:"top",title:k},Object(be.f)(m.a,{className:"pointer",onClick:function(){E(t),w(Ee(t)),f(!0)}},r))))}}}]);