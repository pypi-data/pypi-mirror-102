(window.webpackJsonp=window.webpackJsonp||[]).push([[26],{2847:function(e,t,a){"use strict";a.d(t,"a",(function(){return d}));var n=a(8),l=a.n(n),c=(a(0),a(50)),s=a(51),i=a(47),o=a(1);const r=c.c.span`
  white-space: nowrap;
  min-width: 100px;

  svg,
  i {
    margin-right: 8px;

    &:hover {
      path {
        fill: ${({theme:e})=>e.colors.primary.base};
      }
    }
  }
`;function d({actions:e}){return Object(o.f)(r,{className:"actions"},l()(e).call(e,(e,t)=>e.tooltip?Object(o.f)(s.a,{id:`${e.label}-tooltip`,title:e.tooltip,placement:e.placement,key:t},Object(o.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:e.onClick},Object(o.f)(i.a,{name:e.icon}))):Object(o.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:e.onClick,key:t},Object(o.f)(i.a,{name:e.icon}))))}},3272:function(e,t,a){"use strict";a.r(t);a(38);var n=a(32),l=a.n(n),c=a(8),s=a.n(c),i=a(0),o=a.n(i),r=a(14),d=a(71),b=a(98),m=a.n(b),u=a(28),p=a.n(u),j=a(366),O=a(129),f=a(114),h=a(718),g=a(1088),_=a(51),S=a(1085),y=a(2847),w=a(2842),C=a(50),x=a(47),v=a(95),$=a(201),k=a(1);const D=C.c.div`
  margin: ${({theme:e})=>2*e.gridUnit}px auto
    ${({theme:e})=>4*e.gridUnit}px auto;
`,H=Object(C.c)($.b)`
  border-radius: ${({theme:e})=>e.borderRadius}px;
  border: 1px solid ${({theme:e})=>e.colors.secondary.light2};
`,T=Object(C.c)(x.a)`
  margin: auto ${({theme:e})=>2*e.gridUnit}px auto 0;
`,N=C.c.div`
  margin-bottom: ${({theme:e})=>10*e.gridUnit}px;

  .control-label {
    margin-bottom: ${({theme:e})=>2*e.gridUnit}px;
  }

  .required {
    margin-left: ${({theme:e})=>e.gridUnit/2}px;
    color: ${({theme:e})=>e.colors.error.base};
  }

  input[type='text'] {
    padding: ${({theme:e})=>1.5*e.gridUnit}px
      ${({theme:e})=>2*e.gridUnit}px;
    border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    border-radius: ${({theme:e})=>e.gridUnit}px;
    width: 50%;
  }
`;var A=Object(f.a)(({addDangerToast:e,onCssTemplateAdd:t,onHide:a,show:n,cssTemplate:l=null})=>{const[c,s]=Object(i.useState)(!0),[o,d]=Object(i.useState)(null),[b,m]=Object(i.useState)(!0),u=null!==l,{state:{loading:p,resource:O},fetchResource:f,createResource:h,updateResource:g}=Object(j.f)("css_template",Object(r.e)("css_template"),e),_=()=>{m(!0),a()};return Object(i.useEffect)(()=>{if(u&&(!o||!o.id||l&&l.id!==o.id||b&&n)){if(l&&null!==l.id&&!p){const e=l.id||0;f(e)}}else!u&&(!o||o.id||b&&n)&&d({template_name:"",css:""})},[l]),Object(i.useEffect)(()=>{O&&d(O)},[O]),Object(i.useEffect)(()=>{o&&o.template_name.length&&o.css&&o.css.length?s(!1):s(!0)},[o?o.template_name:"",o?o.css:""]),b&&n&&m(!1),Object(k.f)(v.b,{disablePrimaryButton:c,onHandledPrimaryAction:()=>{if(u){if(o&&o.id){const e=o.id;delete o.id,delete o.created_by,g(e,o).then(e=>{e&&(t&&t(),_())})}}else o&&h(o).then(e=>{e&&(t&&t(),_())})},onHide:_,primaryButtonName:u?Object(r.e)("Save"):Object(r.e)("Add"),show:n,width:"55%",title:Object(k.f)("h4",null,u?Object(k.f)(T,{name:"edit-alt"}):Object(k.f)(T,{name:"plus-large"}),u?Object(r.e)("Edit CSS template properties"):Object(r.e)("Add CSS template"))},Object(k.f)(D,null,Object(k.f)("h4",null,Object(r.e)("Basic information"))),Object(k.f)(N,null,Object(k.f)("div",{className:"control-label"},Object(r.e)("CSS template name"),Object(k.f)("span",{className:"required"},"*")),Object(k.f)("input",{name:"template_name",onChange:e=>{const{target:t}=e,a={...o,template_name:o?o.template_name:"",css:o?o.css:""};a[t.name]=t.value,d(a)},type:"text",value:null==o?void 0:o.template_name})),Object(k.f)(N,null,Object(k.f)("div",{className:"control-label"},Object(r.e)("css"),Object(k.f)("span",{className:"required"},"*")),Object(k.f)(H,{onChange:e=>{const t={...o,template_name:o?o.template_name:"",css:e};d(t)},value:null==o?void 0:o.css,width:"100%"})))});t.default=Object(f.a)((function({addDangerToast:e,addSuccessToast:t,user:a}){const{state:{loading:n,resourceCount:c,resourceCollection:b,bulkSelectEnabled:u},hasPerm:f,fetchData:C,refreshData:x,toggleBulkSelect:v}=Object(j.e)("css_template",Object(r.e)("CSS templates"),e),[$,D]=Object(i.useState)(!1),[H,T]=Object(i.useState)(null),N=f("can_write"),B=f("can_write"),U=f("can_write"),[z,E]=Object(i.useState)(null),M=[{id:"template_name",desc:!0}],q=Object(i.useMemo)(()=>[{accessor:"template_name",Header:Object(r.e)("Name")},{Cell:({row:{original:{changed_on_delta_humanized:e,changed_by:t}}})=>{let a="null";return t&&(a=`${t.first_name} ${t.last_name}`),Object(k.f)(_.a,{id:"allow-run-async-header-tooltip",title:Object(r.e)("Last modified by %s",a),placement:"right"},Object(k.f)("span",null,e))},Header:Object(r.e)("Last modified"),accessor:"changed_on_delta_humanized",size:"xl",disableSortBy:!0},{Cell:({row:{original:{created_on:e}}})=>{const t=new Date(e),a=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate(),t.getHours(),t.getMinutes(),t.getSeconds(),t.getMilliseconds()));return p()(a).fromNow()},Header:Object(r.e)("Created on"),accessor:"created_on",size:"xl",disableSortBy:!0},{accessor:"created_by",disableSortBy:!0,Header:Object(r.e)("Created by"),Cell:({row:{original:{created_by:e}}})=>e?`${e.first_name} ${e.last_name}`:"",size:"xl"},{Cell:({row:{original:e}})=>{var t;const a=l()(t=[B?{label:"edit-action",tooltip:Object(r.e)("Edit template"),placement:"bottom",icon:"edit",onClick:()=>(T(e),void D(!0))}:null,U?{label:"delete-action",tooltip:Object(r.e)("Delete template"),placement:"bottom",icon:"trash",onClick:()=>E(e)}:null]).call(t,e=>!!e);return Object(k.f)(y.a,{actions:a})},Header:Object(r.e)("Actions"),id:"actions",disableSortBy:!0,hidden:!B&&!U,size:"xl"}],[U,N]),P={name:Object(r.e)("CSS templates")},R=[];N&&R.push({name:Object(k.f)(o.a.Fragment,null,Object(k.f)("i",{className:"fa fa-plus"})," ",Object(r.e)("CSS template")),buttonStyle:"primary",onClick:()=>{T(null),D(!0)}}),U&&R.push({name:Object(r.e)("Bulk select"),onClick:v,buttonStyle:"secondary"}),P.buttons=R;const F=Object(i.useMemo)(()=>[{Header:Object(r.e)("Created by"),id:"created_by",input:"select",operator:"rel_o_m",unfilteredLabel:"All",fetchSelects:Object(O.e)("css_template","created_by",Object(O.c)(e=>Object(r.e)("An error occurred while fetching dataset datasource values: %s",e)),a.userId),paginate:!0},{Header:Object(r.e)("Search"),id:"template_name",input:"search",operator:"ct"}],[]);return Object(k.f)(o.a.Fragment,null,Object(k.f)(h.a,P),Object(k.f)(A,{addDangerToast:e,cssTemplate:H,onCssTemplateAdd:()=>x(),onHide:()=>D(!1),show:$}),z&&Object(k.f)(g.a,{description:Object(r.e)("This action will permanently delete the template."),onConfirm:()=>{z&&(({id:a,template_name:n})=>{d.a.delete({endpoint:`/api/v1/css_template/${a}`}).then(()=>{x(),E(null),t(Object(r.e)("Deleted: %s",n))},Object(O.c)(t=>e(Object(r.e)("There was an issue deleting %s: %s",n,t))))})(z)},onHide:()=>E(null),open:!0,title:Object(r.e)("Delete Template?")}),Object(k.f)(S.a,{title:Object(r.e)("Please confirm"),description:Object(r.e)("Are you sure you want to delete the selected templates?"),onConfirm:a=>{d.a.delete({endpoint:`/api/v1/css_template/?q=${m.a.encode(s()(a).call(a,({id:e})=>e))}`}).then(({json:e={}})=>{x(),t(e.message)},Object(O.c)(t=>e(Object(r.e)("There was an issue deleting the selected templates: %s",t))))}},e=>{const t=U?[{key:"delete",name:Object(r.e)("Delete"),onSelect:e,type:"danger"}]:[];return Object(k.f)(w.b,{className:"css-templates-list-view",columns:q,count:c,data:b,fetchData:C,filters:F,initialSort:M,loading:n,pageSize:25,bulkActions:t,bulkSelectEnabled:u,disableBulkSelect:v})}))}))}}]);