(window.webpackJsonp=window.webpackJsonp||[]).push([[28],{115:function(e,t,a){"use strict";a.d(t,"a",(function(){return f})),a.d(t,"b",(function(){return j})),a.d(t,"c",(function(){return g}));var n=a(73),c=a.n(n),l=a(33),o=a.n(l),s=(a(0),a(50)),i=a(1),r=a(22),d=a(47);const b=["fullWidth","allowOverflow"],u=Object(s.c)(r.x,{shouldForwardProp:e=>!o()(b).call(b,e)})`
  overflow: ${({allowOverflow:e})=>e?"visible":"hidden"};

  .ant-tabs-content-holder {
    overflow: ${({allowOverflow:e})=>e?"visible":"auto"};
  }

  .ant-tabs-tab {
    flex: 1 1 auto;

    &.ant-tabs-tab-active .ant-tabs-tab-btn {
      color: inherit;
    }

    &:hover {
      .anchor-link-container {
        cursor: pointer;

        .fa.fa-link {
          visibility: visible;
        }
      }
    }

    .short-link-trigger.btn {
      padding: 0 ${({theme:e})=>e.gridUnit}px;

      & > .fa.fa-link {
        top: 0;
      }
    }
  }

  ${({fullWidth:e})=>e&&i.e`
      .ant-tabs-nav-list {
        width: 100%;
      }

      .ant-tabs-tab {
        width: 0;
      }
    `};

  .ant-tabs-tab-btn {
    display: flex;
    flex: 1 1 auto;
    align-items: center;
    justify-content: center;
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
    text-align: center;
    text-transform: uppercase;
    user-select: none;

    .required {
      margin-left: ${({theme:e})=>e.gridUnit/2}px;
      color: ${({theme:e})=>e.colors.error.base};
    }
  }

  .ant-tabs-ink-bar {
    background: ${({theme:e})=>e.colors.secondary.base};
  }
`,m=Object(s.c)(r.x.TabPane)``,h=c()(u,{TabPane:m});h.defaultProps={fullWidth:!0};const p=Object(s.c)(u)`
  .ant-tabs-content-holder {
    background: white;
  }

  & > .ant-tabs-nav {
    margin-bottom: 0;
  }

  .ant-tabs-tab-remove {
    padding-top: 0;
    padding-bottom: 0;
    height: ${({theme:e})=>6*e.gridUnit}px;
  }

  ${({fullWidth:e})=>e&&i.e`
      .ant-tabs-nav-list {
        width: 100%;
      }
    `}
`,f=c()(p,{TabPane:m});f.defaultProps={type:"editable-card",fullWidth:!1},f.TabPane.defaultProps={closeIcon:Object(i.f)(d.a,{role:"button",tabIndex:0,cursor:"pointer",name:"cancel-x"})};const O=Object(s.c)(f)`
  &.ant-tabs-card > .ant-tabs-nav .ant-tabs-tab {
    margin: 0 ${({theme:e})=>4*e.gridUnit}px;
    padding: ${({theme:e})=>`${3*e.gridUnit}px ${e.gridUnit}px`};
    background: transparent;
    border: none;
  }

  &.ant-tabs-card > .ant-tabs-nav .ant-tabs-ink-bar {
    visibility: visible;
  }

  .ant-tabs-tab-btn {
    font-size: ${({theme:e})=>e.typography.sizes.m}px;
  }

  .ant-tabs-tab-remove {
    margin-left: 0;
    padding-right: 0;
  }

  .ant-tabs-nav-add {
    min-width: unset !important;
    background: transparent !important;
    border: none !important;
  }
`,j=c()(O,{TabPane:m});var g=h},2856:function(e,t,a){"use strict";a(38);var n=a(8),c=a.n(n),l=a(0),o=a.n(l),s=a(50),i=a(14),r=a(47),d=a(95),b=a(366),u=a(1);Object(s.c)(r.a)`
  margin: auto ${({theme:e})=>2*e.gridUnit}px auto 0;
`;const m=s.c.div`
  display: block;
  color: ${({theme:e})=>e.colors.grayscale.base};
  font-size: ${({theme:e})=>e.typography.sizes.s-1}px;
`,h=s.c.div`
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
`;t.a=({resourceName:e,resourceLabel:t,passwordsNeededMessage:a,confirmOverwriteMessage:n,addDangerToast:s,addSuccessToast:r,onModelImport:p,show:f,onHide:O,passwordFields:j=[],setPasswordFields:g=(()=>{})})=>{const[v,y]=Object(l.useState)(!0),[_,w]=Object(l.useState)(null),[x,S]=Object(l.useState)({}),[C,N]=Object(l.useState)(!1),[$,T]=Object(l.useState)(!1),k=Object(l.useRef)(null),q=()=>{w(null),g([]),S({}),N(!1),T(!1),k&&k.current&&(k.current.value="")},{state:{alreadyExists:A,passwordsNeeded:E},importResource:L}=Object(b.d)(e,t,e=>{q(),s(e)});Object(l.useEffect)(()=>{g(E)},[E,g]),Object(l.useEffect)(()=>{N(A.length>0)},[A,N]);const D=e=>{var t,a;const n=null!=(t=null==(a=e.currentTarget)?void 0:a.value)?t:"";T(n.toUpperCase()===Object(i.e)("OVERWRITE"))};return v&&f&&y(!1),Object(u.f)(d.b,{name:"model",className:"import-model-modal",disablePrimaryButton:null===_||C&&!$,onHandledPrimaryAction:()=>{null!==_&&L(_,x,$).then(e=>{e&&(r(Object(i.e)("The import was successful")),q(),p())})},onHide:()=>{y(!0),O(),q()},primaryButtonName:C?Object(i.e)("Overwrite"):Object(i.e)("Import"),primaryButtonType:C?"danger":"primary",width:"750px",show:f,title:Object(u.f)("h4",null,Object(i.e)("Import %s",t))},Object(u.f)(h,null,Object(u.f)("div",{className:"control-label"},Object(u.f)("label",{htmlFor:"modelFile"},Object(i.e)("File"),Object(u.f)("span",{className:"required"},"*"))),Object(u.f)("input",{ref:k,name:"modelFile",id:"modelFile",type:"file",accept:".yaml,.json,.yml,.zip",onChange:e=>{const{files:t}=e.target;w(t&&t[0]||null)}})),0===j.length?null:Object(u.f)(o.a.Fragment,null,Object(u.f)("h5",null,"Database passwords"),Object(u.f)(m,null,a),c()(j).call(j,e=>Object(u.f)(h,{key:`password-for-${e}`},Object(u.f)("div",{className:"control-label"},e,Object(u.f)("span",{className:"required"},"*")),Object(u.f)("input",{name:`password-${e}`,autoComplete:`password-${e}`,type:"password",value:x[e],onChange:t=>S({...x,[e]:t.target.value})})))),C?Object(u.f)(o.a.Fragment,null,Object(u.f)(h,null,Object(u.f)("div",{className:"confirm-overwrite"},n),Object(u.f)("div",{className:"control-label"},Object(i.e)('Type "%s" to confirm',Object(i.e)("OVERWRITE"))),Object(u.f)("input",{id:"overwrite",type:"text",onChange:D}))):null)}},2857:function(e,t,a){"use strict";a.d(t,"a",(function(){return c}));var n=a(14);const c={name:Object(n.e)("Data"),tabs:[{name:"Databases",label:Object(n.e)("Databases"),url:"/databaseview/list/",usesRouter:!0},{name:"Datasets",label:Object(n.e)("Datasets"),url:"/tablemodelview/list/",usesRouter:!0},{name:"Saved queries",label:Object(n.e)("Saved queries"),url:"/savedqueryview/list/",usesRouter:!0},{name:"Query history",label:Object(n.e)("Query history"),url:"/superset/sqllab/history/",usesRouter:!0}]}},3263:function(e,t,a){"use strict";a.r(t);a(38);var n=a(14),c=a(50),l=a(71),o=a(0),s=a.n(o),i=a(98),r=a.n(i),d=a(40),b=a(366),u=a(129),m=a(114),h=a(718),p=a(1088),f=a(51),O=a(47),j=a(2842),g=a(2857),v=a(2856),y=a(256),_=a.n(y),w=a(99),x=a.n(w),S=a(8),C=a.n(S),N=a(80),$=a.n(N),T=a(62),k=a(1);const q=Object(c.c)(f.a)`
  cursor: pointer;

  path:first-of-type {
    fill: #999999;
  }
`,A={fontSize:"12px",lineHeight:"16px"};function E({tooltip:e,placement:t="right",trigger:a="hover",overlayStyle:n=A,bgColor:c="rgba(0,0,0,0.9)"}){return Object(k.f)(q,{title:e,placement:t,trigger:a,overlayStyle:n,color:c},Object(k.f)(O.a,{name:"info-solid-small"}))}var L=a(67),D=a(95),U=a(115),R=a(37),P=a(3031),H=a(201);const I=Object(c.c)(O.a)`
  margin: auto ${({theme:e})=>2*e.gridUnit}px auto 0;
`,z=c.c.div`
  margin-bottom: ${({theme:e})=>2*e.gridUnit}px;

  &.extra-container {
    padding-top: 8px;
  }

  .helper {
    display: block;
    padding: ${({theme:e})=>e.gridUnit}px 0;
    color: ${({theme:e})=>e.colors.grayscale.base};
    font-size: ${({theme:e})=>e.typography.sizes.s-1}px;
    text-align: left;

    .required {
      margin-left: ${({theme:e})=>e.gridUnit/2}px;
      color: ${({theme:e})=>e.colors.error.base};
    }
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
`,Q=Object(c.c)(H.d)`
  flex: 1 1 auto;
  border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
  border-radius: ${({theme:e})=>e.gridUnit}px;
`;var F=Object(m.a)(({addDangerToast:e,addSuccessToast:t,onDatabaseAdd:a,onHide:c,show:s,database:i=null})=>{var r,d,u;const[m,h]=Object(o.useState)(!0),[p,f]=Object(o.useState)(null),[O,j]=Object(o.useState)(!0),[g,v]=Object(o.useState)("1"),y=Object(T.d)(e=>e.common.conf),w=null!==i,{state:{loading:S,resource:N},fetchResource:q,createResource:A,updateResource:H}=Object(b.f)("database",Object(n.e)("database"),e),F=()=>{j(!0),c()},B=e=>{const{target:t}=e,a={database_name:p?p.database_name:"",sqlalchemy_uri:p?p.sqlalchemy_uri:"",...p};var n;"checkbox"===t.type?a[t.name]=t.checked:a[t.name]="string"==typeof t.value?_()(n=t.value).call(n):t.value;f(a)},M=(e,t)=>{const a={database_name:p?p.database_name:"",sqlalchemy_uri:p?p.sqlalchemy_uri:"",...p};a[t]=e,f(a)};if(w&&(!p||!p.id||i&&i.id!==p.id||O&&s)){if(i&&null!==i.id&&!S){const t=i.id||0;v("1"),q(t).then(()=>{f(N)}).catch(t=>e(Object(n.e)("Sorry there was an error fetching database information: %s",t.message)))}}else!w&&(!p||p.id||O&&s)&&(v("1"),f({database_name:"",sqlalchemy_uri:""}));Object(o.useEffect)(()=>{p&&p.database_name.length&&p.sqlalchemy_uri&&p.sqlalchemy_uri.length?h(!1):h(!0)},[p?p.database_name:null,p?p.sqlalchemy_uri:null]),O&&s&&j(!1);return Object(k.f)(D.b,{name:"database",className:"database-modal",disablePrimaryButton:m,onHandledPrimaryAction:()=>{if(w){const e={database_name:p?p.database_name:"",sqlalchemy_uri:p?p.sqlalchemy_uri:"",...p};e.id&&delete e.id,p&&p.id&&H(p.id,e).then(e=>{e&&(a&&a(),F())})}else p&&A(p).then(e=>{e&&(a&&a(),F())})},onHide:F,primaryButtonName:w?Object(n.e)("Save"):Object(n.e)("Add"),width:"750px",show:s,title:Object(k.f)("h4",null,Object(k.f)(I,{name:"database"}),w?Object(n.e)("Edit database"):Object(n.e)("Add database"))},Object(k.f)(U.c,{defaultActiveKey:"1",activeKey:g,onTabClick:e=>{v(e)}},Object(k.f)(U.c.TabPane,{tab:Object(k.f)("span",null,Object(n.e)("Connection"),Object(k.f)("span",{className:"required"},"*")),key:"1"},Object(k.f)(z,null,Object(k.f)("div",{className:"control-label"},Object(n.e)("Database name"),Object(k.f)("span",{className:"required"},"*")),Object(k.f)("div",{className:"input-container"},Object(k.f)("input",{type:"text",name:"database_name",value:p?p.database_name:"",placeholder:Object(n.e)("Name your dataset"),onChange:B}))),Object(k.f)(z,null,Object(k.f)("div",{className:"control-label"},Object(n.e)("SQLAlchemy URI"),Object(k.f)("span",{className:"required"},"*")),Object(k.f)("div",{className:"input-container"},Object(k.f)("input",{type:"text",name:"sqlalchemy_uri",value:p?p.sqlalchemy_uri:"",autoComplete:"off",placeholder:Object(n.e)("dialect+driver://username:password@host:port/database"),onChange:B}),Object(k.f)(R.a,{buttonStyle:"primary",onClick:()=>{if(!p||!p.sqlalchemy_uri||!p.sqlalchemy_uri.length)return void e(Object(n.e)("Please enter a SQLAlchemy URI to test"));const a={sqlalchemy_uri:p?p.sqlalchemy_uri:"",database_name:p&&p.database_name.length?p.database_name:void 0,impersonate_user:p&&p.impersonate_user||void 0,extra:p&&p.extra&&p.extra.length?p.extra:void 0,encrypted_extra:p&&p.encrypted_extra||void 0,server_cert:p&&p.server_cert||void 0};l.a.post({endpoint:"api/v1/database/test_connection",body:$()(a),headers:{"Content-Type":"application/json"}}).then(()=>{t(Object(n.e)("Connection looks good!"))}).catch(t=>Object(L.a)(t).then(t=>{var a;e(null!=t&&t.message?`${Object(n.e)("ERROR: ")}${"string"==typeof t.message?t.message:C()(a=x()(t.message)).call(a,([e,t])=>`(${e}) ${t.join(", ")}`).join("\n")}`:Object(n.e)("ERROR: Connection failed. "))}))},cta:!0},Object(n.e)("Test connection"))),Object(k.f)("div",{className:"helper"},Object(n.e)("Refer to the "),Object(k.f)("a",{href:null!=(r=null==y?void 0:y.SQLALCHEMY_DOCS_URL)?r:"",target:"_blank",rel:"noopener noreferrer"},null!=(d=null==y?void 0:y.SQLALCHEMY_DISPLAY_TEXT)?d:""),Object(n.e)(" for more information on how to structure your URI.")))),Object(k.f)(U.c.TabPane,{tab:Object(k.f)("span",null,Object(n.e)("Performance")),key:"2"},Object(k.f)(z,null,Object(k.f)("div",{className:"control-label"},Object(n.e)("Chart cache timeout")),Object(k.f)("div",{className:"input-container"},Object(k.f)("input",{type:"number",name:"cache_timeout",value:p&&p.cache_timeout||"",placeholder:Object(n.e)("Chart cache timeout"),onChange:B})),Object(k.f)("div",{className:"helper"},Object(n.e)("Duration (in seconds) of the caching timeout for charts of this database. A timeout of 0 indicates that the cache never expires. Note this defaults to the global timeout if undefined."))),Object(k.f)(z,null,Object(k.f)("div",{className:"input-container"},Object(k.f)(P.a,{id:"allow_run_async",indeterminate:!1,checked:!!p&&!!p.allow_run_async,onChange:B}),Object(k.f)("div",null,Object(n.e)("Asynchronous query execution")),Object(k.f)(E,{tooltip:Object(n.e)("Operate the database in asynchronous mode, meaning that the queries are executed on remote workers as opposed to on the web server itself. This assumes that you have a Celery worker setup as well as a results backend. Refer to the installation docs for more information.")})))),Object(k.f)(U.c.TabPane,{tab:Object(k.f)("span",null,Object(n.e)("SQL Lab settings")),key:"3"},Object(k.f)(z,null,Object(k.f)(z,null,Object(k.f)("div",{className:"input-container"},Object(k.f)(P.a,{id:"expose_in_sqllab",indeterminate:!1,checked:!!p&&!!p.expose_in_sqllab,onChange:B}),Object(k.f)("div",null,Object(n.e)("Expose in SQL Lab")),Object(k.f)(E,{tooltip:Object(n.e)("Allow this database to be queried in SQL Lab")}))),Object(k.f)(z,null,Object(k.f)("div",{className:"input-container"},Object(k.f)(P.a,{id:"allow_ctas",indeterminate:!1,checked:!!p&&!!p.allow_ctas,onChange:B}),Object(k.f)("div",null,Object(n.e)("Allow CREATE TABLE AS")),Object(k.f)(E,{tooltip:Object(n.e)("Allow creation of new tables based on queries")}))),Object(k.f)(z,null,Object(k.f)("div",{className:"input-container"},Object(k.f)(P.a,{id:"allow_cvas",indeterminate:!1,checked:!!p&&!!p.allow_cvas,onChange:B}),Object(k.f)("div",null,Object(n.e)("Allow CREATE VIEW AS")),Object(k.f)(E,{tooltip:Object(n.e)("Allow creation of new views based on queries")}))),Object(k.f)(z,null,Object(k.f)("div",{className:"input-container"},Object(k.f)(P.a,{id:"allow_dml",indeterminate:!1,checked:!!p&&!!p.allow_dml,onChange:B}),Object(k.f)("div",null,Object(n.e)("Allow DML")),Object(k.f)(E,{tooltip:Object(n.e)("Allow manipulation of the database using non-SELECT statements such as UPDATE, DELETE, CREATE, etc.")}))),Object(k.f)(z,null,Object(k.f)("div",{className:"input-container"},Object(k.f)(P.a,{id:"allow_multi_schema_metadata_fetch",indeterminate:!1,checked:!!p&&!!p.allow_multi_schema_metadata_fetch,onChange:B}),Object(k.f)("div",null,Object(n.e)("Allow multi schema metadata fetch")),Object(k.f)(E,{tooltip:Object(n.e)("Allow SQL Lab to fetch a list of all tables and all views across all database schemas. For large data warehouse with thousands of tables, this can be expensive and put strain on the system.")})))),Object(k.f)(z,null,Object(k.f)("div",{className:"control-label"},Object(n.e)("CTAS schema")),Object(k.f)("div",{className:"input-container"},Object(k.f)("input",{type:"text",name:"force_ctas_schema",value:p&&p.force_ctas_schema||"",placeholder:Object(n.e)("CTAS schema"),onChange:B})),Object(k.f)("div",{className:"helper"},Object(n.e)("When allowing CREATE TABLE AS option in SQL Lab, this option forces the table to be created in this schema.")))),Object(k.f)(U.c.TabPane,{tab:Object(k.f)("span",null,Object(n.e)("Security")),key:"4"},Object(k.f)(z,null,Object(k.f)("div",{className:"control-label"},Object(n.e)("Secure extra")),Object(k.f)("div",{className:"input-container"},Object(k.f)(Q,{name:"encrypted_extra",value:p&&p.encrypted_extra||"",placeholder:Object(n.e)("Secure extra"),onChange:e=>M(e,"encrypted_extra"),width:"100%",height:"160px"})),Object(k.f)("div",{className:"helper"},Object(k.f)("div",null,Object(n.e)("JSON string containing additional connection configuration.")),Object(k.f)("div",null,Object(n.e)("This is used to provide connection information for systems like Hive, Presto, and BigQuery, which do not conform to the username:password syntax normally used by SQLAlchemy.")))),Object(k.f)(z,null,Object(k.f)("div",{className:"control-label"},Object(n.e)("Root certificate")),Object(k.f)("div",{className:"input-container"},Object(k.f)("textarea",{name:"server_cert",value:p&&p.server_cert||"",placeholder:Object(n.e)("Root certificate"),onChange:e=>{const{target:t}=e,a={database_name:p?p.database_name:"",sqlalchemy_uri:p?p.sqlalchemy_uri:"",...p};a[t.name]=t.value,f(a)}})),Object(k.f)("div",{className:"helper"},Object(n.e)("Optional CA_BUNDLE contents to validate HTTPS requests. Only available on certain database engines.")))),Object(k.f)(U.c.TabPane,{tab:Object(k.f)("span",null,Object(n.e)("Extra")),key:"5"},Object(k.f)(z,null,Object(k.f)("div",{className:"input-container"},Object(k.f)(P.a,{id:"impersonate_user",indeterminate:!1,checked:!!p&&!!p.impersonate_user,onChange:B}),Object(k.f)("div",null,Object(n.e)("Impersonate Logged In User (Presto & Hive)")),Object(k.f)(E,{tooltip:Object(n.e)("If Presto, all the queries in SQL Lab are going to be executed as the currently logged on user who must have permission to run them. If Hive and hive.server2.enable.doAs is enabled, will run the queries as service account, but impersonate the currently logged on user via hive.server2.proxy.user property.")}))),Object(k.f)(z,null,Object(k.f)("div",{className:"input-container"},Object(k.f)(P.a,{id:"allow_csv_upload",indeterminate:!1,checked:!!p&&!!p.allow_csv_upload,onChange:B}),Object(k.f)("div",null,Object(n.e)("Allow data upload")),Object(k.f)(E,{tooltip:Object(n.e)("If selected, please set the schemas allowed for data upload in Extra.")}))),Object(k.f)(z,{className:"extra-container"},Object(k.f)("div",{className:"control-label"},Object(n.e)("Extra")),Object(k.f)("div",{className:"input-container"},Object(k.f)(Q,{name:"extra",value:null!=(u=p&&p.extra)?u:'{\n  "metadata_params": {},\n  "engine_params": {},\n  "metadata_cache_timeout": {},\n  "schemas_allowed_for_csv_upload": [] \n}',placeholder:Object(n.e)("Secure extra"),onChange:e=>M(e,"extra"),width:"100%",height:"160px"})),Object(k.f)("div",{className:"helper"},Object(k.f)("div",null,Object(n.e)("JSON string containing extra configuration elements.")),Object(k.f)("div",null,Object(n.e)("1. The engine_params object gets unpacked into the sqlalchemy.create_engine call, while the metadata_params gets unpacked into the sqlalchemy.MetaData call.")),Object(k.f)("div",null,Object(n.e)('2. The metadata_cache_timeout is a cache timeout setting in seconds for metadata fetch of this database. Specify it as "metadata_cache_timeout": {"schema_cache_timeout": 600, "table_cache_timeout": 600}. If unset, cache will not be enabled for the functionality. A timeout of 0 indicates that the cache never expires.')),Object(k.f)("div",null,Object(n.e)('3. The schemas_allowed_for_csv_upload is a comma separated list of schemas that CSVs are allowed to upload to. Specify it as "schemas_allowed_for_csv_upload": ["public", "csv_upload"]. If database flavor does not support schema or any schema is allowed to be accessed, just leave the list empty.')),Object(k.f)("div",null,Object(n.e)("4. The version field is a string specifying this db's version. This should be used with Presto DBs so that the syntax is correct.")),Object(k.f)("div",null,Object(n.e)("5. The allows_virtual_table_explore field is a boolean specifying whether or not the Explore button in SQL Lab results is shown.")))))))});const B=Object(n.e)('The passwords for the databases below are needed in order to import them. Please note that the "Secure Extra" and "Certificate" sections of the database configuration are not present in export files, and should be added manually after the import if they are needed.'),M=Object(n.e)("You are importing one or more databases that already exist. Overwriting might cause you to lose some of your work. Are you sure you want to overwrite?"),W=Object(c.c)(O.a)`
  color: ${({theme:e})=>e.colors.grayscale.dark1};
`;function V({value:e}){return e?Object(k.f)(W,{name:"check"}):Object(k.f)(W,{name:"cancel-x"})}t.default=Object(m.a)((function({addDangerToast:e,addSuccessToast:t}){const{state:{loading:a,resourceCount:c,resourceCollection:i},hasPerm:m,fetchData:y,refreshData:_}=Object(b.e)("database",Object(n.e)("database"),e),[w,x]=Object(o.useState)(!1),[S,C]=Object(o.useState)(null),[N,$]=Object(o.useState)(null),[T,q]=Object(o.useState)(!1),[A,E]=Object(o.useState)([]),L=()=>{q(!0)},D=m("can_write"),U=m("can_write"),R=m("can_write"),P=m("can_read")&&Object(d.c)(d.a.VERSIONED_EXPORT),H={activeChild:"Databases",...g.a};D&&(H.buttons=[{"data-test":"btn-create-database",name:Object(k.f)(s.a.Fragment,null,Object(k.f)("i",{className:"fa fa-plus"})," ",Object(n.e)("Database")," "),buttonStyle:"primary",onClick:()=>{$(null),x(!0)}}],Object(d.c)(d.a.VERSIONED_EXPORT)&&H.buttons.push({name:Object(k.f)(O.a,{name:"import"}),buttonStyle:"link",onClick:L}));const I=Object(o.useMemo)(()=>[{accessor:"database_name",Header:Object(n.e)("Database")},{accessor:"backend",Header:Object(n.e)("Backend"),size:"lg",disableSortBy:!0},{accessor:"allow_run_async",Header:Object(k.f)(f.a,{id:"allow-run-async-header-tooltip",title:Object(n.e)("Asynchronous query execution"),placement:"top"},Object(k.f)("span",null,Object(n.e)("AQE"))),Cell:({row:{original:{allow_run_async:e}}})=>Object(k.f)(V,{value:e}),size:"sm"},{accessor:"allow_dml",Header:Object(k.f)(f.a,{id:"allow-dml-header-tooltip",title:Object(n.e)("Allow data manipulation language"),placement:"top"},Object(k.f)("span",null,Object(n.e)("DML"))),Cell:({row:{original:{allow_dml:e}}})=>Object(k.f)(V,{value:e}),size:"sm"},{accessor:"allow_csv_upload",Header:Object(n.e)("CSV upload"),Cell:({row:{original:{allow_csv_upload:e}}})=>Object(k.f)(V,{value:e}),size:"md"},{accessor:"expose_in_sqllab",Header:Object(n.e)("Expose in SQL Lab"),Cell:({row:{original:{expose_in_sqllab:e}}})=>Object(k.f)(V,{value:e}),size:"md"},{accessor:"created_by",disableSortBy:!0,Header:Object(n.e)("Created by"),Cell:({row:{original:{created_by:e}}})=>e?`${e.first_name} ${e.last_name}`:"",size:"xl"},{Cell:({row:{original:{changed_on_delta_humanized:e}}})=>e,Header:Object(n.e)("Last modified"),accessor:"changed_on_delta_humanized",size:"xl"},{Cell:({row:{original:e}})=>U||R||P?Object(k.f)("span",{className:"actions"},R&&Object(k.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>{return t=e,l.a.get({endpoint:`/api/v1/database/${t.id}/related_objects/`}).then(({json:e={}})=>{C({...t,chart_count:e.charts.count,dashboard_count:e.dashboards.count})}).catch(Object(u.c)(e=>Object(n.e)("An error occurred while fetching database related data: %s",e)));var t}},Object(k.f)(f.a,{id:"delete-action-tooltip",title:Object(n.e)("Delete database"),placement:"bottom"},Object(k.f)(O.a,{name:"trash"}))),P&&Object(k.f)(f.a,{id:"export-action-tooltip",title:Object(n.e)("Export"),placement:"bottom"},Object(k.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>{return t=e,window.location.assign(`/api/v1/database/export/?q=${r.a.encode([t.id])}`);var t}},Object(k.f)(O.a,{name:"share"}))),U&&Object(k.f)(f.a,{id:"edit-action-tooltip",title:Object(n.e)("Edit"),placement:"bottom"},Object(k.f)("span",{role:"button",tabIndex:0,className:"action-button",onClick:()=>($(e),void x(!0))},Object(k.f)(O.a,{name:"edit-alt"})))):null,Header:Object(n.e)("Actions"),id:"actions",hidden:!U&&!R,disableSortBy:!0}],[R,U,P]),z=Object(o.useMemo)(()=>[{Header:Object(n.e)("Expose in SQL Lab"),id:"expose_in_sqllab",input:"select",operator:"eq",unfilteredLabel:"All",selects:[{label:"Yes",value:!0},{label:"No",value:!1}]},{Header:Object(k.f)(f.a,{id:"allow-run-async-filter-header-tooltip",title:Object(n.e)("Asynchronous query execution"),placement:"top"},Object(k.f)("span",null,Object(n.e)("AQE"))),id:"allow_run_async",input:"select",operator:"eq",unfilteredLabel:"All",selects:[{label:"Yes",value:!0},{label:"No",value:!1}]},{Header:Object(n.e)("Search"),id:"database_name",input:"search",operator:"ct"}],[]);return Object(k.f)(s.a.Fragment,null,Object(k.f)(h.a,H),Object(k.f)(F,{database:N,show:w,onHide:()=>x(!1),onDatabaseAdd:()=>{_()}}),S&&Object(k.f)(p.a,{description:Object(n.e)("The database %s is linked to %s charts that appear on %s dashboards. Are you sure you want to continue? Deleting the database will break those objects.",S.database_name,S.chart_count,S.dashboard_count),onConfirm:()=>{S&&function({id:a,database_name:c}){l.a.delete({endpoint:`/api/v1/database/${a}`}).then(()=>{_(),t(Object(n.e)("Deleted: %s",c)),C(null)},Object(u.c)(t=>e(Object(n.e)("There was an issue deleting %s: %s",c,t))))}(S)},onHide:()=>C(null),open:!0,title:Object(n.e)("Delete Database?")}),Object(k.f)(j.b,{className:"database-list-view",columns:I,count:c,data:i,fetchData:y,filters:z,initialSort:[{id:"changed_on_delta_humanized",desc:!0}],loading:a,pageSize:25}),Object(k.f)(v.a,{resourceName:"database",resourceLabel:Object(n.e)("database"),passwordsNeededMessage:B,confirmOverwriteMessage:M,addDangerToast:e,addSuccessToast:t,onModelImport:()=>{q(!1),_()},show:T,onHide:()=>{q(!1)},passwordFields:A,setPasswordFields:E}))}))}}]);