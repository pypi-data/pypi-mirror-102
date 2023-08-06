(window.webpackJsonp=window.webpackJsonp||[]).push([[77],{167:function(e,t,r){"use strict";r.d(t,"a",(function(){return h}));var a=r(73),o=r.n(a),n=r(50),i=r(969);const c=Object(n.c)(i.a)`
  .ant-radio-inner {
    top: -1px;
    left: 2px;
    width: ${({theme:e})=>4*e.gridUnit}px;
    height: ${({theme:e})=>4*e.gridUnit}px;
    border-width: 2px;
    border-color: ${({theme:e})=>e.colors.grayscale.light2};
  }

  .ant-radio.ant-radio-checked {
    .ant-radio-inner {
      border-width: ${({theme:e})=>e.gridUnit+1}px;
      border-color: ${({theme:e})=>e.colors.primary.base};
    }

    .ant-radio-inner::after {
      background-color: ${({theme:e})=>e.colors.grayscale.light5};
      top: 0;
      left: 0;
      width: ${({theme:e})=>e.gridUnit+2}px;
      height: ${({theme:e})=>e.gridUnit+2}px;
    }
  }

  .ant-radio:hover,
  .ant-radio:focus {
    .ant-radio-inner {
      border-color: ${({theme:e})=>e.colors.primary.dark1};
    }
  }
`,d=Object(n.c)(i.a.Group)`
  font-size: inherit;
`,h=o()(c,{Group:d})},3232:function(e,t,r){"use strict";r.r(t),r.d(t,"default",(function(){return d}));r(38);var a=r(50),o=r(0),n=r(983),i=r(1);const c=a.c.div`
  height: ${({height:e})=>e}px;
  width: ${({width:e})=>e}px;
  overflow-x: scroll;
`;function d(e){const{formData:t,setExtraFormData:r,width:a}=e,{defaultValue:d,currentValue:h}=t,[l,u]=Object(o.useState)(null!=d?d:"Last week"),s=e=>{r({extraFormData:{override_form_data:{time_range:e}},currentState:{value:e}}),u(e)};return Object(o.useEffect)(()=>{s(null!=h?h:"Last week")},[h]),Object(o.useEffect)(()=>{s(null!=d?d:"Last week")},[d]),Object(i.f)(c,{width:a},Object(i.f)(n.a,{value:l,name:"time_range",onChange:s}))}}}]);