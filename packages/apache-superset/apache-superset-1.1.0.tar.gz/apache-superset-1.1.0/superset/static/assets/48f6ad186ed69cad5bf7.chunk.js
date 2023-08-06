(window.webpackJsonp=window.webpackJsonp||[]).push([[23],{2847:function(e,t,a){"use strict";a.d(t,"a",(function(){return d}));var n=a(8),o=a.n(n),c=(a(0),a(50)),l=a(51),i=a(47),r=a(1);const s=c.c.span`
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
`;function d({actions:e}){return Object(r.f)(s,{className:"actions"},o()(e).call(e,(e,t)=>e.tooltip?Object(r.f)(l.a,{id:`${e.label}-tooltip`,title:e.tooltip,placement:e.placement,key:t},Object(r.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:e.onClick},Object(r.f)(i.a,{name:e.icon}))):Object(r.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:e.onClick,key:t},Object(r.f)(i.a,{name:e.icon}))))}},3270:function(e,t,a){"use strict";a.r(t);a(38);var n=a(32),o=a.n(n),c=a(8),l=a.n(c),i=a(0),r=a.n(i),s=a(98),d=a.n(s),b=a(14),u=a(71),m=a(348),j=a(354),O=a(28),p=a.n(O),f=a(366),h=a(129),g=a(114),y=a(718),w=a(2847),x=a(2842),C=a(37),S=a(1088),D=a(1085),v=a(50),_=a(47),$=a(95),k=a(1);const A=v.c.div`
  margin: ${({theme:e})=>2*e.gridUnit}px auto
    ${({theme:e})=>4*e.gridUnit}px auto;
`,H=Object(v.c)(_.a)`
  margin: auto ${({theme:e})=>2*e.gridUnit}px auto 0;
`,M=v.c.div`
  margin-bottom: ${({theme:e})=>10*e.gridUnit}px;

  .control-label {
    margin-bottom: ${({theme:e})=>2*e.gridUnit}px;
  }

  .required {
    margin-left: ${({theme:e})=>e.gridUnit/2}px;
    color: ${({theme:e})=>e.colors.error.base};
  }

  textarea,
  input[type='text'] {
    padding: ${({theme:e})=>1.5*e.gridUnit}px
      ${({theme:e})=>2*e.gridUnit}px;
    border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    border-radius: ${({theme:e})=>e.gridUnit}px;
    width: 50%;
  }

  input,
  textarea {
    flex: 1 1 auto;
  }

  textarea {
    width: 100%;
    height: 160px;
    resize: none;
  }

  input::placeholder,
  textarea::placeholder {
    color: ${({theme:e})=>e.colors.grayscale.light1};
  }
`;var N=Object(g.a)(({addDangerToast:e,onLayerAdd:t,onHide:a,show:n,layer:o=null})=>{const[c,l]=Object(i.useState)(!0),[r,s]=Object(i.useState)(),[d,u]=Object(i.useState)(!0),m=null!==o,{state:{loading:j,resource:O},fetchResource:p,createResource:h,updateResource:g}=Object(f.f)("annotation_layer",Object(b.e)("annotation_layer"),e),y=()=>{u(!0),a()},w=e=>{const{target:t}=e,a={...r,name:r?r.name:"",descr:r?r.descr:""};a[t.name]=t.value,s(a)};if(m&&(!r||!r.id||o&&o.id!==r.id||d&&n)){if(o&&null!==o.id&&!j){p(o.id||0).then(()=>{s(O)})}}else!m&&(!r||r.id||d&&n)&&s({name:"",descr:""});return Object(i.useEffect)(()=>{r&&r.name.length?l(!1):l(!0)},[r?r.name:"",r?r.descr:""]),d&&n&&u(!1),Object(k.f)($.b,{disablePrimaryButton:c,onHandledPrimaryAction:()=>{if(m){if(r&&r.id){const e=r.id;delete r.id,delete r.created_by,g(e,r).then(()=>{y()})}}else r&&h(r).then(e=>{t&&t(e),y()})},onHide:y,primaryButtonName:m?Object(b.e)("Save"):Object(b.e)("Add"),show:n,width:"55%",title:Object(k.f)("h4",null,m?Object(k.f)(H,{name:"edit-alt"}):Object(k.f)(H,{name:"plus-large"}),m?Object(b.e)("Edit annotation layer properties"):Object(b.e)("Add annotation layer"))},Object(k.f)(A,null,Object(k.f)("h4",null,Object(b.e)("Basic information"))),Object(k.f)(M,null,Object(k.f)("div",{className:"control-label"},Object(b.e)("Annotation layer name"),Object(k.f)("span",{className:"required"},"*")),Object(k.f)("input",{name:"name",onChange:w,type:"text",value:null==r?void 0:r.name})),Object(k.f)(M,null,Object(k.f)("div",{className:"control-label"},Object(b.e)("description")),Object(k.f)("textarea",{name:"descr",value:null==r?void 0:r.descr,placeholder:Object(b.e)("Description (this can be seen in the list)"),onChange:w})))});t.default=Object(g.a)((function({addDangerToast:e,addSuccessToast:t,user:a}){const{state:{loading:n,resourceCount:c,resourceCollection:s,bulkSelectEnabled:O},hasPerm:g,fetchData:v,refreshData:_,toggleBulkSelect:$}=Object(f.e)("annotation_layer",Object(b.e)("Annotation layers"),e),[A,H]=Object(i.useState)(!1),[M,U]=Object(i.useState)(null),[Y,T]=Object(i.useState)(null),B=g("can_write"),z=g("can_write"),E=g("can_write");function F(e){U(e),H(!0)}const L=[{id:"name",desc:!0}],P=Object(i.useMemo)(()=>[{accessor:"name",Header:Object(b.e)("Name"),Cell:({row:{original:{id:e,name:t}}})=>{let a=!0;try{Object(m.f)()}catch(e){a=!1}return a?Object(k.f)(j.b,{to:`/annotationmodelview/${e}/annotation`},t):Object(k.f)("a",{href:`/annotationmodelview/${e}/annotation`},t)}},{accessor:"descr",Header:Object(b.e)("Description")},{Cell:({row:{original:{changed_on:e}}})=>{const t=new Date(e),a=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate(),t.getHours(),t.getMinutes(),t.getSeconds(),t.getMilliseconds()));return p()(a).format("MMM DD, YYYY")},Header:Object(b.e)("Last modified"),accessor:"changed_on",size:"xl"},{Cell:({row:{original:{created_on:e}}})=>{const t=new Date(e),a=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate(),t.getHours(),t.getMinutes(),t.getSeconds(),t.getMilliseconds()));return p()(a).format("MMM DD, YYYY")},Header:Object(b.e)("Created on"),accessor:"created_on",size:"xl"},{accessor:"created_by",disableSortBy:!0,Header:Object(b.e)("Created by"),Cell:({row:{original:{created_by:e}}})=>e?`${e.first_name} ${e.last_name}`:"",size:"xl"},{Cell:({row:{original:e}})=>{var t;const a=o()(t=[z?{label:"edit-action",tooltip:Object(b.e)("Edit template"),placement:"bottom",icon:"edit",onClick:()=>F(e)}:null,E?{label:"delete-action",tooltip:Object(b.e)("Delete template"),placement:"bottom",icon:"trash",onClick:()=>T(e)}:null]).call(t,e=>!!e);return Object(k.f)(w.a,{actions:a})},Header:Object(b.e)("Actions"),id:"actions",disableSortBy:!0,hidden:!z&&!E,size:"xl"}],[E,B]),q=[];B&&q.push({name:Object(k.f)(r.a.Fragment,null,Object(k.f)("i",{className:"fa fa-plus"})," ",Object(b.e)("Annotation layer")),buttonStyle:"primary",onClick:()=>{F(null)}}),E&&q.push({name:Object(b.e)("Bulk select"),onClick:$,buttonStyle:"secondary"});const I=Object(i.useMemo)(()=>[{Header:Object(b.e)("Created by"),id:"created_by",input:"select",operator:"rel_o_m",unfilteredLabel:"All",fetchSelects:Object(h.e)("annotation_layer","created_by",Object(h.c)(e=>Object(b.e)("An error occurred while fetching dataset datasource values: %s",e)),a.userId),paginate:!0},{Header:Object(b.e)("Search"),id:"name",input:"search",operator:"ct"}],[]),R=Object(k.f)(C.a,{buttonStyle:"primary",onClick:()=>{F(null)}},Object(k.f)(r.a.Fragment,null,Object(k.f)("i",{className:"fa fa-plus"})," ",Object(b.e)("Annotation layer"))),J={message:Object(b.e)("No annotation layers yet"),slot:R};return Object(k.f)(r.a.Fragment,null,Object(k.f)(y.a,{name:Object(b.e)("Annotation layers"),buttons:q}),Object(k.f)(N,{addDangerToast:e,layer:M,onLayerAdd:e=>{window.location.href=`/annotationmodelview/${e}/annotation`},onHide:()=>H(!1),show:A}),Y&&Object(k.f)(S.a,{description:Object(b.e)("This action will permanently delete the layer."),onConfirm:()=>{Y&&(({id:a,name:n})=>{u.a.delete({endpoint:`/api/v1/annotation_layer/${a}`}).then(()=>{_(),T(null),t(Object(b.e)("Deleted: %s",n))},Object(h.c)(t=>e(Object(b.e)("There was an issue deleting %s: %s",n,t))))})(Y)},onHide:()=>T(null),open:!0,title:Object(b.e)("Delete Layer?")}),Object(k.f)(D.a,{title:Object(b.e)("Please confirm"),description:Object(b.e)("Are you sure you want to delete the selected layers?"),onConfirm:a=>{u.a.delete({endpoint:`/api/v1/annotation_layer/?q=${d.a.encode(l()(a).call(a,({id:e})=>e))}`}).then(({json:e={}})=>{_(),t(e.message)},Object(h.c)(t=>e(Object(b.e)("There was an issue deleting the selected layers: %s",t))))}},e=>{const t=E?[{key:"delete",name:Object(b.e)("Delete"),onSelect:e,type:"danger"}]:[];return Object(k.f)(x.b,{className:"annotation-layers-list-view",columns:P,count:c,data:s,fetchData:v,filters:I,initialSort:L,loading:n,pageSize:25,bulkActions:t,bulkSelectEnabled:O,disableBulkSelect:$,emptyState:J})}))}))}}]);