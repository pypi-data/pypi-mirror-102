(window.webpackJsonp=window.webpackJsonp||[]).push([[29],{2856:function(e,t,a){"use strict";a(38);var n=a(8),s=a.n(n),o=a(0),r=a.n(o),c=a(50),i=a(14),l=a(47),d=a(95),u=a(366),b=a(1);Object(c.c)(l.a)`
  margin: auto ${({theme:e})=>2*e.gridUnit}px auto 0;
`;const h=c.c.div`
  display: block;
  color: ${({theme:e})=>e.colors.grayscale.base};
  font-size: ${({theme:e})=>e.typography.sizes.s-1}px;
`,p=c.c.div`
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
`;t.a=({resourceName:e,resourceLabel:t,passwordsNeededMessage:a,confirmOverwriteMessage:n,addDangerToast:c,addSuccessToast:l,onModelImport:m,show:O,onHide:j,passwordFields:f=[],setPasswordFields:g=(()=>{})})=>{const[y,v]=Object(o.useState)(!0),[w,S]=Object(o.useState)(null),[x,_]=Object(o.useState)({}),[C,k]=Object(o.useState)(!1),[T,D]=Object(o.useState)(!1),N=Object(o.useRef)(null),E=()=>{S(null),g([]),_({}),k(!1),D(!1),N&&N.current&&(N.current.value="")},{state:{alreadyExists:A,passwordsNeeded:H},importResource:$}=Object(u.d)(e,t,e=>{E(),c(e)});Object(o.useEffect)(()=>{g(H)},[H,g]),Object(o.useEffect)(()=>{k(A.length>0)},[A,k]);const R=e=>{var t,a;const n=null!=(t=null==(a=e.currentTarget)?void 0:a.value)?t:"";D(n.toUpperCase()===Object(i.e)("OVERWRITE"))};return y&&O&&v(!1),Object(b.f)(d.b,{name:"model",className:"import-model-modal",disablePrimaryButton:null===w||C&&!T,onHandledPrimaryAction:()=>{null!==w&&$(w,x,T).then(e=>{e&&(l(Object(i.e)("The import was successful")),E(),m())})},onHide:()=>{v(!0),j(),E()},primaryButtonName:C?Object(i.e)("Overwrite"):Object(i.e)("Import"),primaryButtonType:C?"danger":"primary",width:"750px",show:O,title:Object(b.f)("h4",null,Object(i.e)("Import %s",t))},Object(b.f)(p,null,Object(b.f)("div",{className:"control-label"},Object(b.f)("label",{htmlFor:"modelFile"},Object(i.e)("File"),Object(b.f)("span",{className:"required"},"*"))),Object(b.f)("input",{ref:N,name:"modelFile",id:"modelFile",type:"file",accept:".yaml,.json,.yml,.zip",onChange:e=>{const{files:t}=e.target;S(t&&t[0]||null)}})),0===f.length?null:Object(b.f)(r.a.Fragment,null,Object(b.f)("h5",null,"Database passwords"),Object(b.f)(h,null,a),s()(f).call(f,e=>Object(b.f)(p,{key:`password-for-${e}`},Object(b.f)("div",{className:"control-label"},e,Object(b.f)("span",{className:"required"},"*")),Object(b.f)("input",{name:`password-${e}`,autoComplete:`password-${e}`,type:"password",value:x[e],onChange:t=>_({...x,[e]:t.target.value})})))),C?Object(b.f)(r.a.Fragment,null,Object(b.f)(p,null,Object(b.f)("div",{className:"confirm-overwrite"},n),Object(b.f)("div",{className:"control-label"},Object(i.e)('Type "%s" to confirm',Object(i.e)("OVERWRITE"))),Object(b.f)("input",{id:"overwrite",type:"text",onChange:R}))):null)}},2857:function(e,t,a){"use strict";a.d(t,"a",(function(){return s}));var n=a(14);const s={name:Object(n.e)("Data"),tabs:[{name:"Databases",label:Object(n.e)("Databases"),url:"/databaseview/list/",usesRouter:!0},{name:"Datasets",label:Object(n.e)("Datasets"),url:"/tablemodelview/list/",usesRouter:!0},{name:"Saved queries",label:Object(n.e)("Saved queries"),url:"/savedqueryview/list/",usesRouter:!0},{name:"Query history",label:Object(n.e)("Query history"),url:"/superset/sqllab/history/",usesRouter:!0}]}},3273:function(e,t,a){"use strict";a.r(t);a(38);var n=a(54),s=a.n(n),o=a(44),r=a.n(o),c=a(8),i=a.n(c),l=a(14),d=a(50),u=a(71),b=a(0),h=a.n(b),p=a(98),m=a.n(p),O=a(129),j=a(366),f=a(1085),g=a(979),y=a(1088),v=a(2842),w=a(718),S=a(2857),x=a(114),_=a(51),C=a(47),k=a(1092),T=a(1555),D=a(2856),N=a(40),E=a(80),A=a.n(E),H=a(603),$=a.n(H),R=a(652),B=a.n(R),P=a(95),U=a(1556),z=a(1);const F=Object(d.c)(C.a)`
  margin: auto ${({theme:e})=>2*e.gridUnit}px auto 0;
`,I=d.c.div`
  padding-bottom: 340px;
  width: 65%;
`;var q=Object(x.a)(({addDangerToast:e,addSuccessToast:t,onDatasetAdd:a,onHide:n,show:s})=>{const[o,r]=Object(b.useState)(""),[c,i]=Object(b.useState)(""),[d,p]=Object(b.useState)(0),[m,j]=Object(b.useState)(!0);return Object(z.f)(P.b,{disablePrimaryButton:m,onHandledPrimaryAction:()=>{u.a.post({endpoint:"/api/v1/dataset/",body:A()({database:d,...o?{schema:o}:{},table_name:c}),headers:{"Content-Type":"application/json"}}).then(({json:e={}})=>{a&&a({id:e.id,...e.result}),t(Object(l.e)("The dataset has been saved")),n()}).catch(Object(O.c)(t=>e(Object(l.e)("Error while saving dataset: %s",t.table_name))))},onHide:n,primaryButtonName:Object(l.e)("Add"),show:s,title:Object(z.f)(h.a.Fragment,null,Object(z.f)(F,{name:"warning-solid"}),Object(l.e)("Add dataset"))},Object(z.f)(I,null,Object(z.f)(U.a,{clearable:!1,dbId:d,formMode:!0,handleError:e,onChange:({dbId:e,schema:t,tableName:a})=>{p(e),j($()(e)||B()(a)),r(t),i(a)},schema:o,tableName:c})))});const L=Object(l.e)('The passwords for the databases below are needed in order to import them together with the datasets. Please note that the "Secure Extra" and "Certificate" sections of the database configuration are not present in export files, and should be added manually after the import if they are needed.'),M=Object(l.e)("You are importing one or more datasets that already exist. Overwriting might cause you to lose some of your work. Are you sure you want to overwrite?"),V=d.c.div`
  align-items: center;
  display: flex;

  > svg {
    margin-right: ${({theme:e})=>e.gridUnit}px;
  }
`;t.default=Object(x.a)(({addDangerToast:e,addSuccessToast:t,user:a})=>{const{state:{loading:n,resourceCount:o,resourceCollection:c,bulkSelectEnabled:d},hasPerm:p,fetchData:x,toggleBulkSelect:E,refreshData:A}=Object(j.e)("dataset",Object(l.e)("dataset"),e),[H,$]=Object(b.useState)(!1),[R,B]=Object(b.useState)(null),[P,U]=Object(b.useState)(null),[F,I]=Object(b.useState)(!1),[J,W]=Object(b.useState)([]),Q=()=>{I(!0)},X=p("can_write"),Y=p("can_write"),G=p("can_write"),K=p("can_read"),Z=[{id:"changed_on_delta_humanized",desc:!0}],ee=Object(b.useCallback)(({id:t})=>{u.a.get({endpoint:`/api/v1/dataset/${t}`}).then(({json:e={}})=>{var t;const a=i()(t=e.result.owners).call(t,e=>e.id);U({...e.result,owners:a})}).catch(()=>{e(Object(l.e)("An error occurred while fetching dataset related data"))})},[e]),te=Object(b.useMemo)(()=>[{Cell:({row:{original:{kind:e}}})=>"physical"===e?Object(z.f)(_.a,{id:"physical-dataset-tooltip",title:Object(l.e)("Physical dataset")},Object(z.f)(C.a,{name:"dataset-physical"})):Object(z.f)(_.a,{id:"virtual-dataset-tooltip",title:Object(l.e)("Virtual dataset")},Object(z.f)(C.a,{name:"dataset-virtual"})),accessor:"kind_icon",disableSortBy:!0,size:"xs"},{Cell:({row:{original:{extra:e,table_name:t,explore_url:a}}})=>{const n=Object(z.f)("a",{href:a},t);try{const t=JSON.parse(e);return null!=t&&t.certification?Object(z.f)(V,null,Object(z.f)(T.a,{certifiedBy:t.certification.certified_by,details:t.certification.details}),n):n}catch{return n}},Header:Object(l.e)("Name"),accessor:"table_name"},{Cell:({row:{original:{kind:e}}})=>{var t;return(null==(t=e[0])?void 0:t.toUpperCase())+r()(e).call(e,1)},Header:Object(l.e)("Type"),accessor:"kind",disableSortBy:!0,size:"md"},{Header:Object(l.e)("Source"),accessor:"database.database_name",size:"lg"},{Header:Object(l.e)("Schema"),accessor:"schema",size:"lg"},{Cell:({row:{original:{changed_on_delta_humanized:e}}})=>Object(z.f)("span",{className:"no-wrap"},e),Header:Object(l.e)("Modified"),accessor:"changed_on_delta_humanized",size:"xl"},{Cell:({row:{original:{changed_by_name:e}}})=>e,Header:Object(l.e)("Modified by"),accessor:"changed_by.first_name",size:"xl"},{accessor:"database",disableSortBy:!0,hidden:!0},{Cell:({row:{original:{owners:e=[],table_name:t}}})=>Object(z.f)(k.a,{users:e}),Header:Object(l.e)("Owners"),id:"owners",disableSortBy:!0,size:"lg"},{accessor:"sql",hidden:!0,disableSortBy:!0},{Cell:({row:{original:e}})=>X||Y||K?Object(z.f)("span",{className:"actions"},Y&&Object(z.f)(_.a,{id:"delete-action-tooltip",title:Object(l.e)("Delete"),placement:"bottom"},Object(z.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>{return t=e,u.a.get({endpoint:`/api/v1/dataset/${t.id}/related_objects`}).then(({json:e={}})=>{B({...t,chart_count:e.charts.count,dashboard_count:e.dashboards.count})}).catch(Object(O.c)(e=>Object(l.e)("An error occurred while fetching dataset related data: %s",e)));var t}},Object(z.f)(C.a,{name:"trash"}))),K&&Object(z.f)(_.a,{id:"export-action-tooltip",title:Object(l.e)("Export"),placement:"bottom"},Object(z.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>oe([e])},Object(z.f)(C.a,{name:"share"}))),X&&Object(z.f)(_.a,{id:"edit-action-tooltip",title:Object(l.e)("Edit"),placement:"bottom"},Object(z.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>ee(e)},Object(z.f)(C.a,{name:"edit-alt"})))):null,Header:Object(l.e)("Actions"),id:"actions",hidden:!X&&!Y,disableSortBy:!0}],[X,Y,K,ee]),ae=Object(b.useMemo)(()=>[{Header:Object(l.e)("Owner"),id:"owners",input:"select",operator:"rel_m_m",unfilteredLabel:"All",fetchSelects:Object(O.e)("dataset","owners",Object(O.c)(e=>Object(l.e)("An error occurred while fetching dataset owner values: %s",e)),a.userId),paginate:!0},{Header:Object(l.e)("Database"),id:"database",input:"select",operator:"rel_o_m",unfilteredLabel:"All",fetchSelects:Object(O.e)("dataset","database",Object(O.c)(e=>Object(l.e)("An error occurred while fetching datasets: %s",e))),paginate:!0},{Header:Object(l.e)("Schema"),id:"schema",input:"select",operator:"eq",unfilteredLabel:"All",fetchSelects:Object(O.d)("dataset","schema",Object(O.c)(e=>Object(l.e)("An error occurred while fetching schema values: %s",e))),paginate:!0},{Header:Object(l.e)("Type"),id:"sql",input:"select",operator:"dataset_is_null_or_empty",unfilteredLabel:"All",selects:[{label:"Virtual",value:!1},{label:"Physical",value:!0}]},{Header:Object(l.e)("Search"),id:"table_name",input:"search",operator:"ct"}],[]),ne={activeChild:"Datasets",...S.a},se=[];(Y||K)&&se.push({name:Object(l.e)("Bulk select"),onClick:E,buttonStyle:"secondary"}),G&&se.push({name:Object(z.f)(h.a.Fragment,null,Object(z.f)("i",{className:"fa fa-plus"})," ",Object(l.e)("Dataset")," "),onClick:()=>$(!0),buttonStyle:"primary"}),Object(N.c)(N.a.VERSIONED_EXPORT)&&se.push({name:Object(z.f)(C.a,{name:"import"}),buttonStyle:"link",onClick:Q}),ne.buttons=se;const oe=e=>window.location.assign(`/api/v1/dataset/export/?q=${m.a.encode(i()(e).call(e,({id:e})=>e))}`);return Object(z.f)(h.a.Fragment,null,Object(z.f)(w.a,ne),Object(z.f)(q,{show:H,onHide:()=>$(!1),onDatasetAdd:A}),R&&Object(z.f)(y.a,{description:Object(l.e)("The dataset %s is linked to %s charts that appear on %s dashboards. Are you sure you want to continue? Deleting the dataset will break those objects.",R.table_name,R.chart_count,R.dashboard_count),onConfirm:()=>{R&&(({id:a,table_name:n})=>{u.a.delete({endpoint:`/api/v1/dataset/${a}`}).then(()=>{A(),B(null),t(Object(l.e)("Deleted: %s",n))},Object(O.c)(t=>e(Object(l.e)("There was an issue deleting %s: %s",n,t))))})(R)},onHide:()=>{B(null)},open:!0,title:Object(l.e)("Delete Dataset?")}),P&&Object(z.f)(g.a,{datasource:P,onDatasourceSave:A,onHide:()=>{U(null)},show:!0}),Object(z.f)(f.a,{title:Object(l.e)("Please confirm"),description:Object(l.e)("Are you sure you want to delete the selected datasets?"),onConfirm:a=>{u.a.delete({endpoint:`/api/v1/dataset/?q=${m.a.encode(i()(a).call(a,({id:e})=>e))}`}).then(({json:e={}})=>{A(),t(e.message)},Object(O.c)(t=>e(Object(l.e)("There was an issue deleting the selected datasets: %s",t))))}},e=>{const t=[];return Y&&t.push({key:"delete",name:Object(l.e)("Delete"),onSelect:e,type:"danger"}),K&&t.push({key:"export",name:Object(l.e)("Export"),type:"primary",onSelect:oe}),Object(z.f)(v.b,{className:"dataset-list-view",columns:te,data:c,count:o,pageSize:25,fetchData:x,filters:ae,loading:n,initialSort:Z,bulkActions:t,bulkSelectEnabled:d,disableBulkSelect:E,renderBulkSelectCopy:e=>{const{virtualCount:t,physicalCount:a}=s()(e).call(e,(e,t)=>("physical"===t.original.kind?e.physicalCount+=1:"virtual"===t.original.kind&&(e.virtualCount+=1),e),{virtualCount:0,physicalCount:0});return e.length?t&&!a?Object(l.e)("%s Selected (Virtual)",e.length,t):a&&!t?Object(l.e)("%s Selected (Physical)",e.length,a):Object(l.e)("%s Selected (%s Physical, %s Virtual)",e.length,a,t):Object(l.e)("0 Selected")}})}),Object(z.f)(D.a,{resourceName:"dataset",resourceLabel:Object(l.e)("dataset"),passwordsNeededMessage:L,confirmOverwriteMessage:M,addDangerToast:e,addSuccessToast:t,onModelImport:()=>{I(!1),A()},show:F,onHide:()=>{I(!1)},passwordFields:J,setPasswordFields:W}))})},634:function(e,t,a){"use strict";var n=a(31),s=a.n(n),o=a(9),r=a.n(o),c=a(0),i=a.n(c),l=a(2),d=a.n(l),u=a(77),b=a(14),h=a(71),p=a(67),m=a(1);const O={dataEndpoint:d.a.string.isRequired,onChange:d.a.func.isRequired,mutator:d.a.func.isRequired,onAsyncError:d.a.func,value:d.a.oneOfType([d.a.number,d.a.arrayOf(d.a.number)]),valueRenderer:d.a.func,placeholder:d.a.string,autoSelect:d.a.bool},j={placeholder:Object(b.e)("Select ..."),onAsyncError:()=>{}};class f extends i.a.PureComponent{constructor(e){var t;super(e),this.state={isLoading:!1,options:[]},this.onChange=r()(t=this.onChange).call(t,this)}componentDidMount(){this.fetchOptions()}onChange(e){this.props.onChange(e)}fetchOptions(){this.setState({isLoading:!0});const{mutator:e,dataEndpoint:t}=this.props;return h.a.get({endpoint:t}).then(({json:t})=>{const a=e?e(t):t;this.setState({options:a,isLoading:!1}),!this.props.value&&this.props.autoSelect&&a.length>0&&this.onChange(a[0])}).catch(e=>Object(p.a)(e).then(e=>{this.props.onAsyncError(e.error||e.statusText||e),this.setState({isLoading:!1})}))}render(){return Object(m.f)(u.f,s()({placeholder:this.props.placeholder,options:this.state.options,value:this.props.value,isLoading:this.state.isLoading,onChange:this.onChange,valueRenderer:this.props.valueRenderer},this.props))}}f.propTypes=O,f.defaultProps=j,t.a=f},979:function(e,t,a){"use strict";a(38);var n=a(8),s=a.n(n),o=a(80),r=a.n(o),c=a(0),i=a.n(c),l=a(171),d=a(37),u=a(50),b=a(71),h=a(14),p=a(95),m=a(327),O=a(40),j=a(67),f=a(114),g=a(1);const y=Object(m.a)(()=>Promise.all([a.e(0),a.e(14),a.e(16),a.e(69)]).then(a.bind(null,1925))),v=Object(u.c)(p.b)`
  .modal-content {
    height: 900px;
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }

  .modal-header {
    flex: 0 1 auto;
  }
  .modal-body {
    flex: 1 1 auto;
    overflow: auto;
  }

  .modal-footer {
    flex: 0 1 auto;
  }
`;function w(e){var t,a;return null!=e&&e.certified_by||null!=e&&e.certification_details?r()({certification:{certified_by:null!=(t=null==e?void 0:e.certified_by)?t:null,details:null!=(a=null==e?void 0:e.certification_details)?a:null}}):null}t.a=Object(f.a)(({addSuccessToast:e,datasource:t,onDatasourceSave:a,onHide:n,show:o})=>{const[r,u]=Object(c.useState)(t),[m,f]=Object(c.useState)([]),[S,x]=Object(c.useState)(!1),_=Object(c.useRef)(null),[C,k]=p.b.useModal(),T=()=>{var t,o,c;const i=(null==(t=r.tableSelector)?void 0:t.schema)||(null==(o=r.databaseSelector)?void 0:o.schema)||r.schema;x(!0),b.a.post({endpoint:"/datasource/save/",postPayload:{data:{...r,schema:i,metrics:null==r?void 0:null==(c=r.metrics)?void 0:s()(c).call(c,e=>({...e,extra:w(e)})),type:r.type||r.datasource_type}}}).then(({json:t})=>{e(Object(h.e)("The dataset has been saved")),a(t),n()}).catch(e=>{x(!1),Object(j.a)(e).then(({error:e})=>{C.error({title:"Error",content:e||Object(h.e)("An error has occurred"),okButtonProps:{danger:!0,className:"btn-danger"}})})})};return Object(g.f)(v,{show:o,onHide:n,title:Object(g.f)("span",null,Object(h.e)("Edit Dataset "),Object(g.f)("strong",null,r.table_name)),footer:Object(g.f)(i.a.Fragment,null,Object(O.c)(O.a.ENABLE_REACT_CRUD_VIEWS)&&Object(g.f)(d.a,{buttonSize:"small",buttonStyle:"default",className:"m-r-5",onClick:()=>{window.location.href=r.edit_url||r.url}},Object(h.e)("Use legacy datasource editor")),Object(g.f)(d.a,{buttonSize:"small",className:"m-r-5",onClick:n},Object(h.e)("Cancel")),Object(g.f)(d.a,{buttonSize:"small",buttonStyle:"primary",onClick:()=>{_.current=C.confirm({title:Object(h.e)("Confirm save"),content:Object(g.f)("div",null,Object(g.f)(l.a,{css:e=>({marginTop:4*e.gridUnit,marginBottom:4*e.gridUnit}),type:"warning",showIcon:!0,message:Object(h.e)("The dataset configuration exposed here\n                affects all the charts using this dataset.\n                Be mindful that changing settings\n                here may affect other charts\n                in undesirable ways.")}),Object(h.e)("Are you sure you want to save and apply changes?")),onOk:T,icon:null})},disabled:S||m.length>0},Object(h.e)("Save"))),responsive:!0},Object(g.f)(y,{showLoadingForImport:!0,height:500,datasource:r,onChange:(e,t)=>{var a;u({...e,metrics:null==e?void 0:s()(a=e.metrics).call(a,e=>({...e,is_certified:(null==e?void 0:e.certified_by)||(null==e?void 0:e.certification_details)}))}),f(t)}}),k)})}}]);