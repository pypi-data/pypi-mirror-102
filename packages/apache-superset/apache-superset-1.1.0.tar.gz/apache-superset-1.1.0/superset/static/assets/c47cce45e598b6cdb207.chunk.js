(window.webpackJsonp=window.webpackJsonp||[]).push([[25],{2856:function(e,t,a){"use strict";a(38);var r=a(8),c=a.n(r),l=a(0),n=a.n(l),o=a(50),i=a(14),s=a(47),d=a(95),b=a(366),u=a(1);Object(o.c)(s.a)`
  margin: auto ${({theme:e})=>2*e.gridUnit}px auto 0;
`;const m=o.c.div`
  display: block;
  color: ${({theme:e})=>e.colors.grayscale.base};
  font-size: ${({theme:e})=>e.typography.sizes.s-1}px;
`,p=o.c.div`
  padding-bottom: ${({theme:e})=>2*e.gridUnit}px;
  padding-top: ${({theme:e})=>2*e.gridUnit}px;

  & > div {
    margin: ${({theme:e})=>e.gridUnit}px 0;
  }

  &.extra-container {
    padding-top: 8px;
  }

  .confirm-overwrite {
    margin-bottom: ${({theme:e})=>2*e.gridUnit}px;
  }

  .input-container {
    display: flex;
    align-items: center;

    label {
      display: flex;
      margin-right: ${({theme:e})=>2*e.gridUnit}px;
    }

    i {
      margin: 0 ${({theme:e})=>e.gridUnit}px;
    }
  }

  input,
  textarea {
    flex: 1 1 auto;
  }

  textarea {
    height: 160px;
    resize: none;
  }

  input::placeholder,
  textarea::placeholder {
    color: ${({theme:e})=>e.colors.grayscale.light1};
  }

  textarea,
  input[type='text'],
  input[type='number'] {
    padding: ${({theme:e})=>1.5*e.gridUnit}px
      ${({theme:e})=>2*e.gridUnit}px;
    border-style: none;
    border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    border-radius: ${({theme:e})=>e.gridUnit}px;

    &[name='name'] {
      flex: 0 1 auto;
      width: 40%;
    }

    &[name='sqlalchemy_uri'] {
      margin-right: ${({theme:e})=>3*e.gridUnit}px;
    }
  }
`;t.a=({resourceName:e,resourceLabel:t,passwordsNeededMessage:a,confirmOverwriteMessage:r,addDangerToast:o,addSuccessToast:s,onModelImport:O,show:h,onHide:j,passwordFields:f=[],setPasswordFields:g=(()=>{})})=>{const[y,w]=Object(l.useState)(!0),[_,v]=Object(l.useState)(null),[x,S]=Object(l.useState)({}),[C,E]=Object(l.useState)(!1),[k,N]=Object(l.useState)(!1),z=Object(l.useRef)(null),$=()=>{v(null),g([]),S({}),E(!1),N(!1),z&&z.current&&(z.current.value="")},{state:{alreadyExists:T,passwordsNeeded:F},importResource:H}=Object(b.d)(e,t,e=>{$(),o(e)});Object(l.useEffect)(()=>{g(F)},[F,g]),Object(l.useEffect)(()=>{E(T.length>0)},[T,E]);const A=e=>{var t,a;const r=null!=(t=null==(a=e.currentTarget)?void 0:a.value)?t:"";N(r.toUpperCase()===Object(i.e)("OVERWRITE"))};return y&&h&&w(!1),Object(u.f)(d.b,{name:"model",className:"import-model-modal",disablePrimaryButton:null===_||C&&!k,onHandledPrimaryAction:()=>{null!==_&&H(_,x,k).then(e=>{e&&(s(Object(i.e)("The import was successful")),$(),O())})},onHide:()=>{w(!0),j(),$()},primaryButtonName:C?Object(i.e)("Overwrite"):Object(i.e)("Import"),primaryButtonType:C?"danger":"primary",width:"750px",show:h,title:Object(u.f)("h4",null,Object(i.e)("Import %s",t))},Object(u.f)(p,null,Object(u.f)("div",{className:"control-label"},Object(u.f)("label",{htmlFor:"modelFile"},Object(i.e)("File"),Object(u.f)("span",{className:"required"},"*"))),Object(u.f)("input",{ref:z,name:"modelFile",id:"modelFile",type:"file",accept:".yaml,.json,.yml,.zip",onChange:e=>{const{files:t}=e.target;v(t&&t[0]||null)}})),0===f.length?null:Object(u.f)(n.a.Fragment,null,Object(u.f)("h5",null,"Database passwords"),Object(u.f)(m,null,a),c()(f).call(f,e=>Object(u.f)(p,{key:`password-for-${e}`},Object(u.f)("div",{className:"control-label"},e,Object(u.f)("span",{className:"required"},"*")),Object(u.f)("input",{name:`password-${e}`,autoComplete:`password-${e}`,type:"password",value:x[e],onChange:t=>S({...x,[e]:t.target.value})})))),C?Object(u.f)(n.a.Fragment,null,Object(u.f)(p,null,Object(u.f)("div",{className:"confirm-overwrite"},r),Object(u.f)("div",{className:"control-label"},Object(i.e)('Type "%s" to confirm',Object(i.e)("OVERWRITE"))),Object(u.f)("input",{id:"overwrite",type:"text",onChange:A}))):null)}},3188:function(e,t,a){var r=a(815),c=a(1562);e.exports=function(e,t){return e&&e.length?c(e,r(t,2)):[]}},3241:function(e,t,a){"use strict";a.r(t);a(38);var r=a(221),c=a.n(r),l=a(211),n=a.n(l),o=a(8),i=a.n(o),s=a(3188),d=a.n(s),b=a(14),u=a(272),m=a(71),p=a(0),O=a.n(p),h=a(98),j=a.n(h),f=a(40),g=a(129),y=a(366),w=a(1085),_=a(718),v=a(47),x=a(669),S=a(2842),C=a(114),E=a(1057),k=a(2856),N=a(51),z=a(1875),$=a(1);const T=Object(b.e)('The passwords for the databases below are needed in order to import them together with the charts. Please note that the "Secure Extra" and "Certificate" sections of the database configuration are not present in export files, and should be added manually after the import if they are needed.'),F=Object(b.e)("You are importing one or more charts that already exist. Overwriting might cause you to lose some of your work. Are you sure you want to overwrite?"),H=Object(u.a)();t.default=Object(C.a)((function(e){var t,a;const{addDangerToast:r,addSuccessToast:l}=e,{state:{loading:o,resourceCount:s,resourceCollection:u,bulkSelectEnabled:h},setResourceCollection:C,hasPerm:A,fetchData:D,toggleBulkSelect:I,refreshData:M}=Object(y.e)("chart",Object(b.e)("chart"),r),U=Object(p.useMemo)(()=>i()(u).call(u,e=>e.id),[u]),[R,B]=Object(y.c)("chart",U,r),{sliceCurrentlyEditing:L,handleChartUpdated:P,openChartEditModal:V,closeChartEditModal:q}=Object(y.b)(C,u),[W,J]=Object(p.useState)(!1),[X,Y]=Object(p.useState)([]),G=()=>{J(!0)},K=A("can_write"),Q=A("can_write"),Z=A("can_write"),ee=A("can_read")&&Object(f.c)(f.a.VERSIONED_EXPORT),te=[{id:"changed_on_delta_humanized",desc:!0}],ae=Object(p.useMemo)(()=>[{Cell:({row:{original:{id:e}}})=>Object($.f)(x.a,{itemId:e,saveFaveStar:R,isStarred:B[e]}),Header:"",id:"id",disableSortBy:!0,size:"xs"},{Cell:({row:{original:{url:e,slice_name:t}}})=>Object($.f)("a",{href:e},t),Header:Object(b.e)("Chart"),accessor:"slice_name"},{Cell:({row:{original:{viz_type:e}}})=>{var t;return(null==(t=H.get(e))?void 0:t.name)||e},Header:Object(b.e)("Visualization type"),accessor:"viz_type",size:"xxl"},{Cell:({row:{original:{datasource_name_text:e,datasource_url:t}}})=>Object($.f)("a",{href:t},e),Header:Object(b.e)("Dataset"),accessor:"datasource_id",disableSortBy:!0,size:"xl"},{Cell:({row:{original:{changed_by_name:e,changed_by_url:t}}})=>Object($.f)("a",{href:t},e),Header:Object(b.e)("Modified by"),accessor:"changed_by.first_name",size:"xl"},{Cell:({row:{original:{changed_on_delta_humanized:e}}})=>Object($.f)("span",{className:"no-wrap"},e),Header:Object(b.e)("Last modified"),accessor:"changed_on_delta_humanized",size:"xl"},{accessor:"owners",hidden:!0,disableSortBy:!0},{Cell:({row:{original:{created_by:e}}})=>e?`${e.first_name} ${e.last_name}`:"",Header:Object(b.e)("Created by"),accessor:"created_by",disableSortBy:!0,size:"xl"},{Cell:({row:{original:e}})=>Q||Z||ee?Object($.f)("span",{className:"actions"},Z&&Object($.f)(w.a,{title:Object(b.e)("Please confirm"),description:Object($.f)(O.a.Fragment,null,Object(b.e)("Are you sure you want to delete")," ",Object($.f)("b",null,e.slice_name),"?"),onConfirm:()=>Object(g.i)(e,l,r,M)},e=>Object($.f)(N.a,{id:"delete-action-tooltip",title:Object(b.e)("Delete"),placement:"bottom"},Object($.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:e},Object($.f)(v.a,{name:"trash"})))),ee&&Object($.f)(N.a,{id:"export-action-tooltip",title:Object(b.e)("Export"),placement:"bottom"},Object($.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>Object(g.g)([e])},Object($.f)(v.a,{name:"share"}))),Q&&Object($.f)(N.a,{id:"edit-action-tooltip",title:Object(b.e)("Edit"),placement:"bottom"},Object($.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>V(e)},Object($.f)(v.a,{name:"edit-alt"})))):null,Header:Object(b.e)("Actions"),id:"actions",disableSortBy:!0,hidden:!Q&&!Z}],[Q,Z,ee,B]),re=[{Header:Object(b.e)("Owner"),id:"owners",input:"select",operator:S.a.relationManyMany,unfilteredLabel:Object(b.e)("All"),fetchSelects:Object(g.e)("chart","owners",Object(g.c)(e=>r(Object(b.e)("An error occurred while fetching chart owners values: %s",e))),e.user.userId),paginate:!0},{Header:Object(b.e)("Created by"),id:"created_by",input:"select",operator:S.a.relationOneMany,unfilteredLabel:Object(b.e)("All"),fetchSelects:Object(g.e)("chart","created_by",Object(g.c)(e=>r(Object(b.e)("An error occurred while fetching chart created by values: %s",e))),e.user.userId),paginate:!0},{Header:Object(b.e)("Viz type"),id:"viz_type",input:"select",operator:S.a.equals,unfilteredLabel:Object(b.e)("All"),selects:n()(t=i()(a=c()(H).call(H)).call(a,e=>{var t;return{label:(null==(t=H.get(e))?void 0:t.name)||e,value:e}})).call(t,(e,t)=>e.label&&t.label?e.label>t.label?1:e.label<t.label?-1:0:0)},{Header:Object(b.e)("Dataset"),id:"datasource_id",input:"select",operator:S.a.equals,unfilteredLabel:Object(b.e)("All"),fetchSelects:(ce=Object(g.c)(e=>r(Object(b.e)("An error occurred while fetching chart dataset values: %s",e))),async(e="",t,a)=>{const r=e?{filters:[{col:"table_name",opr:"sw",value:e}]}:{};try{var c;const e=j.a.encode({columns:["datasource_name","datasource_id"],keys:["none"],order_column:"table_name",order_direction:"asc",...t?{page:t}:{},...a?{page_size:a}:{},...r}),{json:l={}}=await m.a.get({endpoint:`/api/v1/dataset/?q=${e}`}),n=null==l?void 0:null==(c=l.result)?void 0:i()(c).call(c,({table_name:e,id:t})=>({label:e,value:t}));return d()(n,"value")}catch(e){ce(e)}return[]}),paginate:!1},{Header:Object(b.e)("Favorite"),id:"id",urlDisplay:"favorite",input:"select",operator:S.a.chartIsFav,unfilteredLabel:Object(b.e)("Any"),selects:[{label:Object(b.e)("Yes"),value:!0},{label:Object(b.e)("No"),value:!1}]},{Header:Object(b.e)("Search"),id:"slice_name",input:"search",operator:S.a.chartAllText}];var ce;const le=[{desc:!1,id:"slice_name",label:Object(b.e)("Alphabetical"),value:"alphabetical"},{desc:!0,id:"changed_on_delta_humanized",label:Object(b.e)("Recently modified"),value:"recently_modified"},{desc:!1,id:"changed_on_delta_humanized",label:Object(b.e)("Least recently modified"),value:"least_recently_modified"}];function ne(e){return Object($.f)(z.a,{chart:e,hasPerm:A,openChartEditModal:V,bulkSelectEnabled:h,addDangerToast:r,addSuccessToast:l,refreshData:M,loading:o,favoriteStatus:B[e.id],saveFavoriteStatus:R})}const oe=[];return(Z||ee)&&oe.push({name:Object(b.e)("Bulk select"),buttonStyle:"secondary","data-test":"bulk-select",onClick:I}),K&&oe.push({name:Object($.f)(O.a.Fragment,null,Object($.f)("i",{className:"fa fa-plus"})," ",Object(b.e)("Chart")),buttonStyle:"primary",onClick:()=>{window.location.assign("/chart/add")}}),Object(f.c)(f.a.VERSIONED_EXPORT)&&oe.push({name:Object($.f)(v.a,{name:"import"}),buttonStyle:"link",onClick:G}),Object($.f)(O.a.Fragment,null,Object($.f)(_.a,{name:Object(b.e)("Charts"),buttons:oe}),L&&Object($.f)(E.a,{onHide:q,onSave:P,show:!0,slice:L}),Object($.f)(w.a,{title:Object(b.e)("Please confirm"),description:Object(b.e)("Are you sure you want to delete the selected charts?"),onConfirm:function(e){m.a.delete({endpoint:`/api/v1/chart/?q=${j.a.encode(i()(e).call(e,({id:e})=>e))}`}).then(({json:e={}})=>{M(),l(e.message)},Object(g.c)(e=>r(Object(b.e)("There was an issue deleting the selected charts: %s",e))))}},e=>{const t=[];return Z&&t.push({key:"delete",name:Object(b.e)("Delete"),type:"danger",onSelect:e}),ee&&t.push({key:"export",name:Object(b.e)("Export"),type:"primary",onSelect:g.g}),Object($.f)(S.b,{bulkActions:t,bulkSelectEnabled:h,cardSortSelectOptions:le,className:"chart-list-view",columns:ae,count:s,data:u,disableBulkSelect:I,fetchData:D,filters:re,initialSort:te,loading:o,pageSize:25,renderCard:ne,defaultViewMode:Object(f.c)(f.a.LISTVIEWS_DEFAULT_CARD_VIEW)?"card":"table"})}),Object($.f)(k.a,{resourceName:"chart",resourceLabel:Object(b.e)("chart"),passwordsNeededMessage:T,confirmOverwriteMessage:F,addDangerToast:r,addSuccessToast:l,onModelImport:()=>{J(!1),M()},show:W,onHide:()=>{J(!1)},passwordFields:X,setPasswordFields:Y}))}))}}]);