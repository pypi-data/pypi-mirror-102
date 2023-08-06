(window.webpackJsonp=window.webpackJsonp||[]).push([[27],{2856:function(e,t,a){"use strict";a(38);var r=a(8),o=a.n(r),l=a(0),s=a.n(l),n=a(50),c=a(14),i=a(47),d=a(95),b=a(366),u=a(1);Object(n.c)(i.a)`
  margin: auto ${({theme:e})=>2*e.gridUnit}px auto 0;
`;const O=n.c.div`
  display: block;
  color: ${({theme:e})=>e.colors.grayscale.base};
  font-size: ${({theme:e})=>e.typography.sizes.s-1}px;
`,h=n.c.div`
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
`;t.a=({resourceName:e,resourceLabel:t,passwordsNeededMessage:a,confirmOverwriteMessage:r,addDangerToast:n,addSuccessToast:i,onModelImport:p,show:m,onHide:j,passwordFields:f=[],setPasswordFields:g=(()=>{})})=>{const[y,w]=Object(l.useState)(!0),[S,x]=Object(l.useState)(null),[_,v]=Object(l.useState)({}),[C,k]=Object(l.useState)(!1),[N,$]=Object(l.useState)(!1),E=Object(l.useRef)(null),F=()=>{x(null),g([]),v({}),k(!1),$(!1),E&&E.current&&(E.current.value="")},{state:{alreadyExists:T,passwordsNeeded:D},importResource:H}=Object(b.d)(e,t,e=>{F(),n(e)});Object(l.useEffect)(()=>{g(D)},[D,g]),Object(l.useEffect)(()=>{k(T.length>0)},[T,k]);const I=e=>{var t,a;const r=null!=(t=null==(a=e.currentTarget)?void 0:a.value)?t:"";$(r.toUpperCase()===Object(c.e)("OVERWRITE"))};return y&&m&&w(!1),Object(u.f)(d.b,{name:"model",className:"import-model-modal",disablePrimaryButton:null===S||C&&!N,onHandledPrimaryAction:()=>{null!==S&&H(S,_,N).then(e=>{e&&(i(Object(c.e)("The import was successful")),F(),p())})},onHide:()=>{w(!0),j(),F()},primaryButtonName:C?Object(c.e)("Overwrite"):Object(c.e)("Import"),primaryButtonType:C?"danger":"primary",width:"750px",show:m,title:Object(u.f)("h4",null,Object(c.e)("Import %s",t))},Object(u.f)(h,null,Object(u.f)("div",{className:"control-label"},Object(u.f)("label",{htmlFor:"modelFile"},Object(c.e)("File"),Object(u.f)("span",{className:"required"},"*"))),Object(u.f)("input",{ref:E,name:"modelFile",id:"modelFile",type:"file",accept:".yaml,.json,.yml,.zip",onChange:e=>{const{files:t}=e.target;x(t&&t[0]||null)}})),0===f.length?null:Object(u.f)(s.a.Fragment,null,Object(u.f)("h5",null,"Database passwords"),Object(u.f)(O,null,a),o()(f).call(f,e=>Object(u.f)(h,{key:`password-for-${e}`},Object(u.f)("div",{className:"control-label"},e,Object(u.f)("span",{className:"required"},"*")),Object(u.f)("input",{name:`password-${e}`,autoComplete:`password-${e}`,type:"password",value:_[e],onChange:t=>v({..._,[e]:t.target.value})})))),C?Object(u.f)(s.a.Fragment,null,Object(u.f)(h,null,Object(u.f)("div",{className:"confirm-overwrite"},r),Object(u.f)("div",{className:"control-label"},Object(c.e)('Type "%s" to confirm',Object(c.e)("OVERWRITE"))),Object(u.f)("input",{id:"overwrite",type:"text",onChange:I}))):null)}},3242:function(e,t,a){"use strict";a.r(t);a(38);var r=a(8),o=a.n(r),l=a(14),s=a(71),n=a(0),c=a.n(n),i=a(98),d=a.n(i),b=a(40),u=a(129),O=a(366),h=a(1085),p=a(718),m=a(2842),j=a(114),f=a(1092),g=a(47),y=a(669),w=a(1058),S=a(51),x=a(2856),_=a(1876),v=a(1);const C=Object(l.e)('The passwords for the databases below are needed in order to import them together with the dashboards. Please note that the "Secure Extra" and "Certificate" sections of the database configuration are not present in export files, and should be added manually after the import if they are needed.'),k=Object(l.e)("You are importing one or more dashboards that already exist. Overwriting might cause you to lose some of your work. Are you sure you want to overwrite?");t.default=Object(j.a)((function(e){const{addDangerToast:t,addSuccessToast:a}=e,{state:{loading:r,resourceCount:i,resourceCollection:j,bulkSelectEnabled:N},setResourceCollection:$,hasPerm:E,fetchData:F,toggleBulkSelect:T,refreshData:D}=Object(O.e)("dashboard",Object(l.e)("dashboard"),t),H=Object(n.useMemo)(()=>o()(j).call(j,e=>e.id),[j]),[I,z]=Object(O.c)("dashboard",H,t),[A,M]=Object(n.useState)(null),[U,P]=Object(n.useState)(!1),[R,B]=Object(n.useState)([]),L=()=>{P(!0)},V=E("can_write"),q=E("can_write"),W=E("can_write"),J=E("can_read"),Y=[{id:"changed_on_delta_humanized",desc:!0}];function X(e){M(e)}function G(e){return s.a.get({endpoint:`/api/v1/dashboard/${e.id}`}).then(({json:e={}})=>{$(o()(j).call(j,t=>t.id===e.id?e.result:t))},Object(u.c)(e=>t(Object(l.e)("An error occurred while fetching dashboards: %s",e))))}const K=Object(n.useMemo)(()=>[{Cell:({row:{original:{id:e}}})=>Object(v.f)(y.a,{itemId:e,saveFaveStar:I,isStarred:z[e]}),Header:"",id:"id",disableSortBy:!0,size:"xs"},{Cell:({row:{original:{url:e,dashboard_title:t}}})=>Object(v.f)("a",{href:e},t),Header:Object(l.e)("Title"),accessor:"dashboard_title"},{Cell:({row:{original:{changed_by_name:e,changed_by_url:t}}})=>Object(v.f)("a",{href:t},e),Header:Object(l.e)("Modified by"),accessor:"changed_by.first_name",size:"xl"},{Cell:({row:{original:{published:e}}})=>e?Object(l.e)("Published"):Object(l.e)("Draft"),Header:Object(l.e)("Status"),accessor:"published",size:"xl"},{Cell:({row:{original:{changed_on_delta_humanized:e}}})=>Object(v.f)("span",{className:"no-wrap"},e),Header:Object(l.e)("Modified"),accessor:"changed_on_delta_humanized",size:"xl"},{Cell:({row:{original:{created_by:e}}})=>e?`${e.first_name} ${e.last_name}`:"",Header:Object(l.e)("Created by"),accessor:"created_by",disableSortBy:!0,size:"xl"},{Cell:({row:{original:{owners:e=[]}}})=>Object(v.f)(f.a,{users:e}),Header:Object(l.e)("Owners"),accessor:"owners",disableSortBy:!0,size:"xl"},{Cell:({row:{original:e}})=>Object(v.f)("span",{className:"actions"},W&&Object(v.f)(h.a,{title:Object(l.e)("Please confirm"),description:Object(v.f)(c.a.Fragment,null,Object(l.e)("Are you sure you want to delete")," ",Object(v.f)("b",null,e.dashboard_title),"?"),onConfirm:()=>Object(u.j)(e,D,a,t)},e=>Object(v.f)(S.a,{id:"delete-action-tooltip",title:Object(l.e)("Delete"),placement:"bottom"},Object(v.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:e},Object(v.f)(g.a,{name:"trash"})))),J&&Object(v.f)(S.a,{id:"export-action-tooltip",title:Object(l.e)("Export"),placement:"bottom"},Object(v.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>Object(u.h)([e])},Object(v.f)(g.a,{name:"share"}))),q&&Object(v.f)(S.a,{id:"edit-action-tooltip",title:Object(l.e)("Edit"),placement:"bottom"},Object(v.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>X(e)},Object(v.f)(g.a,{name:"edit-alt"})))),Header:Object(l.e)("Actions"),id:"actions",hidden:!q&&!W&&!J,disableSortBy:!0}],[q,W,J,z]),Q=[{Header:Object(l.e)("Owner"),id:"owners",input:"select",operator:m.a.relationManyMany,unfilteredLabel:Object(l.e)("All"),fetchSelects:Object(u.e)("dashboard","owners",Object(u.c)(e=>t(Object(l.e)("An error occurred while fetching dashboard owner values: %s",e))),e.user.userId),paginate:!0},{Header:Object(l.e)("Created by"),id:"created_by",input:"select",operator:m.a.relationOneMany,unfilteredLabel:Object(l.e)("All"),fetchSelects:Object(u.e)("dashboard","created_by",Object(u.c)(e=>t(Object(l.e)("An error occurred while fetching dashboard created by values: %s",e))),e.user.userId),paginate:!0},{Header:Object(l.e)("Status"),id:"published",input:"select",operator:m.a.equals,unfilteredLabel:Object(l.e)("Any"),selects:[{label:Object(l.e)("Published"),value:!0},{label:Object(l.e)("Unpublished"),value:!1}]},{Header:Object(l.e)("Favorite"),id:"id",urlDisplay:"favorite",input:"select",operator:m.a.dashboardIsFav,unfilteredLabel:Object(l.e)("Any"),selects:[{label:Object(l.e)("Yes"),value:!0},{label:Object(l.e)("No"),value:!1}]},{Header:Object(l.e)("Search"),id:"dashboard_title",input:"search",operator:m.a.titleOrSlug}],Z=[{desc:!1,id:"dashboard_title",label:Object(l.e)("Alphabetical"),value:"alphabetical"},{desc:!0,id:"changed_on_delta_humanized",label:Object(l.e)("Recently modified"),value:"recently_modified"},{desc:!1,id:"changed_on_delta_humanized",label:Object(l.e)("Least recently modified"),value:"least_recently_modified"}];function ee(e){return Object(v.f)(_.a,{dashboard:e,hasPerm:E,bulkSelectEnabled:N,refreshData:D,loading:r,addDangerToast:t,addSuccessToast:a,openDashboardEditModal:X,saveFavoriteStatus:I,favoriteStatus:z[e.id]})}const te=[];return(W||J)&&te.push({name:Object(l.e)("Bulk select"),buttonStyle:"secondary","data-test":"bulk-select",onClick:T}),V&&te.push({name:Object(v.f)(c.a.Fragment,null,Object(v.f)("i",{className:"fa fa-plus"})," ",Object(l.e)("Dashboard")),buttonStyle:"primary",onClick:()=>{window.location.assign("/dashboard/new")}}),Object(b.c)(b.a.VERSIONED_EXPORT)&&te.push({name:Object(v.f)(g.a,{name:"import"}),buttonStyle:"link",onClick:L}),Object(v.f)(c.a.Fragment,null,Object(v.f)(p.a,{name:Object(l.e)("Dashboards"),buttons:te}),Object(v.f)(h.a,{title:Object(l.e)("Please confirm"),description:Object(l.e)("Are you sure you want to delete the selected dashboards?"),onConfirm:function(e){return s.a.delete({endpoint:`/api/v1/dashboard/?q=${d.a.encode(o()(e).call(e,({id:e})=>e))}`}).then(({json:e={}})=>{D(),a(e.message)},Object(u.c)(e=>t(Object(l.e)("There was an issue deleting the selected dashboards: ",e))))}},e=>{const t=[];return W&&t.push({key:"delete",name:Object(l.e)("Delete"),type:"danger",onSelect:e}),J&&t.push({key:"export",name:Object(l.e)("Export"),type:"primary",onSelect:u.h}),Object(v.f)(c.a.Fragment,null,A&&Object(v.f)(w.a,{dashboardId:A.id,show:!0,onHide:()=>M(null),onSubmit:G}),Object(v.f)(m.b,{bulkActions:t,bulkSelectEnabled:N,cardSortSelectOptions:Z,className:"dashboard-list-view",columns:K,count:i,data:j,disableBulkSelect:T,fetchData:F,filters:Q,initialSort:Y,loading:r,pageSize:25,renderCard:ee,defaultViewMode:Object(b.c)(b.a.LISTVIEWS_DEFAULT_CARD_VIEW)?"card":"table"}))}),Object(v.f)(x.a,{resourceName:"dashboard",resourceLabel:Object(l.e)("dashboard"),passwordsNeededMessage:C,confirmOverwriteMessage:k,addDangerToast:t,addSuccessToast:a,onModelImport:()=>{P(!1),D()},show:U,onHide:()=>{P(!1)},passwordFields:R,setPasswordFields:B}))}))}}]);