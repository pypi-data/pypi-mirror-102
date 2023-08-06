(window.webpackJsonp=window.webpackJsonp||[]).push([[14],{115:function(e,t,n){"use strict";n.d(t,"a",(function(){return g})),n.d(t,"b",(function(){return v})),n.d(t,"c",(function(){return C}));var o=n(73),a=n.n(o),s=n(33),r=n.n(s),l=(n(0),n(50)),i=n(1),c=n(22),h=n(47);const p=["fullWidth","allowOverflow"],d=Object(l.c)(c.x,{shouldForwardProp:e=>!r()(p).call(p,e)})`
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
`,u=Object(l.c)(c.x.TabPane)``,b=a()(d,{TabPane:u});b.defaultProps={fullWidth:!0};const f=Object(l.c)(d)`
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
`,g=a()(f,{TabPane:u});g.defaultProps={type:"editable-card",fullWidth:!1},g.TabPane.defaultProps={closeIcon:Object(i.f)(h.a,{role:"button",tabIndex:0,cursor:"pointer",name:"cancel-x"})};const m=Object(l.c)(g)`
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
`,v=a()(m,{TabPane:u});var C=b},166:function(e,t,n){"use strict";n.d(t,"c",(function(){return o})),n.d(t,"f",(function(){return a})),n.d(t,"b",(function(){return s})),n.d(t,"a",(function(){return r})),n.d(t,"g",(function(){return l})),n.d(t,"d",(function(){return i})),n.d(t,"e",(function(){return c}));const o="YYYY-MM-DD HH:mm:ssZ",a="HH:mm:ss.SSS",s="True",r="False",l={standalone:"standalone",preselectFilters:"preselect_filters"},i=250,c=500},167:function(e,t,n){"use strict";n.d(t,"a",(function(){return c}));var o=n(73),a=n.n(o),s=n(50),r=n(969);const l=Object(s.c)(r.a)`
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
`,i=Object(s.c)(r.a.Group)`
  font-size: inherit;
`,c=a()(l,{Group:i})},185:function(e,t,n){"use strict";n.d(t,"a",(function(){return u}));var o=n(9),a=n.n(o),s=n(0),r=n.n(s),l=n(2),i=n.n(l),c=n(95),h=n(37),p=n(1);const d={dialogClassName:i.a.string,triggerNode:i.a.node.isRequired,modalTitle:i.a.node,modalBody:i.a.node,modalFooter:i.a.node,beforeOpen:i.a.func,onExit:i.a.func,isButton:i.a.bool,className:i.a.string,tooltip:i.a.string,width:i.a.string,maxWidth:i.a.string,responsive:i.a.bool};class u extends r.a.Component{constructor(e){var t,n;super(e),this.state={showModal:!1},this.open=a()(t=this.open).call(t,this),this.close=a()(n=this.close).call(n,this)}close(){this.setState(()=>({showModal:!1}))}open(e){e.preventDefault(),this.props.beforeOpen(),this.setState(()=>({showModal:!0}))}renderModal(){return Object(p.f)(c.b,{wrapClassName:this.props.dialogClassName,className:this.props.className,show:this.state.showModal,onHide:this.close,afterClose:this.props.onExit,title:this.props.modalTitle,footer:this.props.modalFooter,hideFooter:!this.props.modalFooter,width:this.props.width,maxWidth:this.props.maxWidth,responsive:this.props.responsive},this.props.modalBody)}render(){return this.props.isButton?Object(p.f)(r.a.Fragment,null,Object(p.f)(h.a,{className:"modal-trigger",tooltip:this.props.tooltip,onClick:this.open},this.props.triggerNode),this.renderModal()):Object(p.f)(r.a.Fragment,null,Object(p.f)("span",{onClick:this.open,role:"button"},this.props.triggerNode),this.renderModal())}}u.propTypes=d,u.defaultProps={beforeOpen:()=>{},onExit:()=>{},isButton:!1,className:"",modalTitle:""}},328:function(e,t,n){"use strict";n.d(t,"a",(function(){return m}));var o=n(133),a=n.n(o),s=n(544),r=n.n(s),l=n(0),i=n.n(l),c=n(589),h=n(555),p=n(1007),d=n(709),u=n(159),b=n.n(u),f=n(83),g=n(1);class m extends i.a.Component{constructor(e){var t;super(e),this.debouncedOnChange=b()(e=>{this.onChange(e)},500),this.onChange=e=>{var t,n;let o=e;const s=[];if(""!==e&&this.props.isFloat){const t=Object(p.a)(e);t?s.push(t):o=e.match(/.*([.0])$/g)?e:r()(e)}if(""!==e&&this.props.isInt){const t=Object(d.a)(e);t?s.push(t):o=a()(e,10)}null==(t=(n=this.props).onChange)||t.call(n,o,s)},this.onChangeWrapper=e=>{const{value:t}=e.target;this.setState({value:t}),(this.props.renderTrigger?this.debouncedOnChange:this.onChange)(t)},this.render=()=>{const{value:e}=this.state,t=null!=e?e.toString():"";return Object(g.f)("div",null,Object(g.f)(f.a,this.props),Object(g.f)(c.a,{controlId:this.state.controlId,bsSize:"medium"},Object(g.f)(h.a,{type:"text",placeholder:this.props.placeholder,onChange:this.onChangeWrapper,onFocus:this.props.onFocus,value:t,disabled:this.props.disabled})))},this.state={controlId:(t=e.controlId,`formInlineName_${null!=t?t:(1e6*Math.random()).toFixed()}`),value:e.value,currentDatasource:e.datasource}}static getDerivedStateFromProps(e,t){return e.value!==t.value&&e.datasource!==t.currentDatasource?{value:e.value,currentDatasource:e.datasource}:null}}},331:function(e,t,n){"use strict";n.d(t,"a",(function(){return g}));var o=n(31),a=n.n(o),s=n(9),r=n.n(s),l=n(0),i=n.n(l),c=n(2),h=n.n(c),p=n(83),d=n(638),u=n(1);const b={value:h.a.bool,label:h.a.string,onChange:h.a.func},f={paddingRight:"5px"};class g extends i.a.Component{onChange(){this.props.onChange(!this.props.value)}renderCheckbox(){var e;return Object(u.f)(d.a,{onChange:r()(e=this.onChange).call(e,this),style:f,checked:!!this.props.value})}render(){var e;return this.props.label?Object(u.f)(p.a,a()({},this.props,{leftNode:this.renderCheckbox(),onClick:r()(e=this.onChange).call(e,this)})):this.renderCheckbox()}}g.propTypes=b,g.defaultProps={value:!1,onChange:()=>{}}},342:function(e,t,n){"use strict";n.d(t,"a",(function(){return i}));n(0);var o=n(2),a=n.n(o),s=n(112),r=n(1);const l={title:a.a.string.isRequired,isSelected:a.a.bool.isRequired,onSelect:a.a.func.isRequired,info:a.a.string,children:a.a.node.isRequired};function i({title:e,isSelected:t,children:n,onSelect:o,info:a}){return Object(r.f)("div",{className:`PopoverSection ${t?"":"dimmed"}`},Object(r.f)("div",{role:"button",tabIndex:0,onClick:o,className:"pointer"},Object(r.f)("strong",null,e),"  ",a&&Object(r.f)(s.a,{tooltip:a,label:"date-free-tooltip"})," ",Object(r.f)("i",{className:t?"fa fa-check text-primary":""})),Object(r.f)("div",{className:"m-t-5 m-l-5"},n))}i.propTypes=l},389:function(e,t,n){"use strict";n.d(t,"a",(function(){return F}));n(38);var o=n(31),a=n.n(o),s=n(357),r=n.n(s),l=n(70),i=n.n(l),c=n(1158),h=n.n(c),p=n(53),d=n.n(p),u=n(32),b=n.n(u),f=n(8),g=n.n(f),m=n(26),v=n.n(m),C=n(9),O=n.n(C),j=n(0),y=n.n(j),x=n(2),w=n.n(x),k=n(14),S=n(77),T=n(83),R=n(1);const $={autoFocus:w.a.bool,choices:w.a.array,clearable:w.a.bool,description:w.a.string,disabled:w.a.bool,freeForm:w.a.bool,isLoading:w.a.bool,label:w.a.string,multi:w.a.bool,isMulti:w.a.bool,allowAll:w.a.bool,name:w.a.string.isRequired,onChange:w.a.func,onFocus:w.a.func,value:w.a.oneOfType([w.a.string,w.a.number,w.a.array]),showHeader:w.a.bool,optionRenderer:w.a.func,valueRenderer:w.a.func,valueKey:w.a.string,options:w.a.array,placeholder:w.a.string,noResultsText:w.a.string,selectRef:w.a.func,filterOption:w.a.func,promptTextCreator:w.a.func,commaChoosesOption:w.a.bool,menuPortalTarget:w.a.element,menuPosition:w.a.string,menuPlacement:w.a.string,forceOverflow:w.a.bool},M={autoFocus:!1,choices:[],clearable:!0,description:null,disabled:!1,freeForm:!1,isLoading:!1,label:null,multi:!1,onChange:()=>{},onFocus:()=>{},showHeader:!0,valueKey:"value",noResultsText:Object(k.e)("No results found"),promptTextCreator:e=>`Create Option ${e}`,commaChoosesOption:!0,allowAll:!1};class F extends y.a.PureComponent{constructor(e){var t,n,o,a;super(e),this.state={options:this.getOptions(e),value:this.props.value},this.onChange=O()(t=this.onChange).call(t,this),this.createMetaSelectAllOption=O()(n=this.createMetaSelectAllOption).call(n,this),this.select=null,this.getSelectRef=O()(o=this.getSelectRef).call(o,this),this.handleKeyDownForCreate=O()(a=this.handleKeyDownForCreate).call(a,this)}UNSAFE_componentWillReceiveProps(e){if(e.choices!==this.props.choices||e.options!==this.props.options){const t=this.getOptions(e);this.setState({options:t})}}onChange(e){let t=this.props.multi?[]:null;if(e)if(this.props.multi)v()(e).call(e,e=>{var n,o;!0!==e.meta?t.push(e[this.props.valueKey]||e):t=g()(n=b()(o=this.getOptions(this.props)).call(o,e=>!e.meta)).call(n,e=>e[this.props.valueKey])});else{if(!0===e.meta)return;t=e[this.props.valueKey]}this.props.onChange(t)}getSelectRef(e){this.select=e,this.props.selectRef&&this.props.selectRef(e)}getOptions(e){let t=[];var n;if(e.options)t=g()(n=e.options).call(n,e=>e);else if(e.choices){var o;t=g()(o=e.choices).call(o,t=>{if(d()(t)){const[n,o]=t.length>1?t:[t[0],t[0]];return{label:o,[e.valueKey]:n}}return h()(t)?t:{label:t,[e.valueKey]:t}})}if(e.freeForm&&e.value){const n=new i.a(g()(t).call(t,t=>t[e.valueKey])),o=d()(e.value)?e.value:[e.value];v()(o).call(o,o=>{n.has(o)||t.unshift({label:o,[e.valueKey]:o})})}return!0===e.allowAll&&!0===e.multi?this.optionsIncludesSelectAll(t)||t.unshift(this.createMetaSelectAllOption()):t=b()(t).call(t,e=>!this.isMetaSelectAllOption(e)),t}handleKeyDownForCreate(e){const{key:t}=e;("Tab"===t||this.props.commaChoosesOption&&","===t)&&this.select&&this.select.onKeyDown({...e,key:"Enter"})}isMetaSelectAllOption(e){return e.meta&&!0===e.meta&&"Select all"===e.label}optionsIncludesSelectAll(e){return r()(e).call(e,e=>this.isMetaSelectAllOption(e))>=0}optionsRemaining(){const{options:e}=this.state,{value:t}=this.props;let n=d()(t)?e.length-t.length:e.length;return this.optionsIncludesSelectAll(e)&&(n-=1),n}createMetaSelectAllOption(){const e={label:"Select all",meta:!0};return e[this.props.valueKey]="Select all",e}render(){const{autoFocus:e,clearable:t,disabled:n,filterOption:o,isLoading:s,menuPlacement:r,name:l,noResultsText:i,onFocus:c,optionRenderer:h,promptTextCreator:p,value:u,valueKey:b,valueRenderer:f,forceOverflow:g,menuPortalTarget:m,menuPosition:v}=this.props,C=this.optionsRemaining(),O=C?Object(k.e)("%s option(s)",C):"",j=this.props.placeholder||O,y=this.props.isMulti||this.props.multi;let x;y&&C&&d()(this.state.value)&&d()(u)&&u.length&&(x=O);const w={autoFocus:e,clearable:t,disabled:n,filterOption:o,ignoreAccents:!1,isLoading:s,isMulti:y,labelKey:"label",menuPlacement:r,forceOverflow:g,menuPortalTarget:m,menuPosition:v,name:`select-${l}`,noResultsText:i,onChange:this.onChange,onFocus:c,optionRenderer:h,value:u,options:this.state.options,placeholder:j,assistiveText:x,promptTextCreator:p,selectRef:this.getSelectRef,valueKey:b,valueRenderer:f};let $;return this.props.freeForm?($=S.c,w.onKeyDown=this.handleKeyDownForCreate):$=S.f,Object(R.f)("div",null,this.props.showHeader&&Object(R.f)(T.a,this.props),y?Object(R.f)(S.d,a()({},w,{selectWrap:$})):Object(R.f)($,w))}}F.propTypes=$,F.defaultProps=M},638:function(e,t,n){"use strict";n.d(t,"a",(function(){return l}));n(0);var o=n(50),a=n(650),s=n(1);const r=o.c.span`
  &,
  & svg {
    vertical-align: top;
  }
`;function l({checked:e,onChange:t,style:n}){return Object(s.f)(r,{style:n,onClick:()=>{t(!e)},role:"checkbox",tabIndex:0,"aria-checked":e,"aria-label":"Checkbox"},e?Object(s.f)(a.a,null):Object(s.f)(a.c,null))}},650:function(e,t,n){"use strict";n.d(t,"a",(function(){return a})),n.d(t,"b",(function(){return s})),n.d(t,"c",(function(){return r}));n(0);var o=n(1);const a=()=>Object(o.f)("svg",{width:"18",height:"18",viewBox:"0 0 18 18",fill:"none",xmlns:"http://www.w3.org/2000/svg"},Object(o.f)("path",{d:"M16 0H2C0.89 0 0 0.9 0 2V16C0 17.1 0.89 18 2 18H16C17.11 18 18 17.1 18 16V2C18 0.9 17.11 0 16 0Z",fill:"#20A7C9"}),Object(o.f)("path",{d:"M7 14L2 9L3.41 7.59L7 11.17L14.59 3.58L16 5L7 14Z",fill:"white"})),s=()=>Object(o.f)("svg",{width:"18",height:"18",viewBox:"0 0 18 18",fill:"none",xmlns:"http://www.w3.org/2000/svg"},Object(o.f)("path",{d:"M16 0H2C0.9 0 0 0.9 0 2V16C0 17.1 0.9 18 2 18H16C17.1 18 18 17.1 18 16V2C18 0.9 17.1 0 16 0Z",fill:"#999999"}),Object(o.f)("path",{d:"M14 10H4V8H14V10Z",fill:"white"})),r=()=>Object(o.f)("svg",{width:"18",height:"18",viewBox:"0 0 18 18",fill:"none",xmlns:"http://www.w3.org/2000/svg"},Object(o.f)("path",{d:"M16 0H2C0.9 0 0 0.9 0 2V16C0 17.1 0.9 18 2 18H16C17.1 18 18 17.1 18 16V2C18 0.9 17.1 0 16 0Z",fill:"#CCCCCC"}),Object(o.f)("path",{d:"M16 2V16H2V2H16V2Z",fill:"white"}))},974:function(e,t,n){"use strict";n.d(t,"a",(function(){return j}));var o=n(9),a=n.n(o),s=n(159),r=n.n(s),l=n(0),i=n.n(l),c=n(2),h=n.n(c),p=n(589),d=n(555),u=n(14),b=n(166),f=n(37),g=n(201),m=n(185),v=n(83),C=n(1);const O={name:h.a.string,onChange:h.a.func,value:h.a.string,height:h.a.number,minLines:h.a.number,maxLines:h.a.number,offerEditInModal:h.a.bool,language:h.a.oneOf([null,"json","html","sql","markdown","javascript"]),aboveEditorSection:h.a.node,readOnly:h.a.bool};class j extends i.a.Component{constructor(){super(),this.onAceChangeDebounce=r()(e=>{this.onAceChange(e)},b.d)}onControlChange(e){this.props.onChange(e.target.value)}onAceChange(e){this.props.onChange(e)}renderEditor(e=!1){var t;const n=this.props.value||"",o=e?40:this.props.minLines||12;if(this.props.language){const t={border:"1px solid #CCC"};return this.props.readOnly&&(t.backgroundColor="#f2f2f2"),Object(C.f)(g.g,{mode:this.props.language,style:t,minLines:o,maxLines:e?1e3:this.props.maxLines,onChange:this.onAceChangeDebounce,width:"100%",height:`${o}em`,editorProps:{$blockScrolling:!0},value:n,readOnly:this.props.readOnly})}return Object(C.f)(p.a,{controlId:"formControlsTextarea"},Object(C.f)(d.a,{componentClass:"textarea",placeholder:Object(u.e)("textarea"),onChange:a()(t=this.onControlChange).call(t,this),value:n,disabled:this.props.readOnly,style:{height:this.props.height}}))}renderModalBody(){return Object(C.f)("div",null,Object(C.f)("div",null,this.props.aboveEditorSection),this.renderEditor(!0))}render(){const e=Object(C.f)(v.a,this.props);return Object(C.f)("div",null,e,this.renderEditor(),this.props.offerEditInModal&&Object(C.f)(m.a,{modalTitle:e,triggerNode:Object(C.f)(f.a,{buttonSize:"small",className:"m-t-5"},Object(u.e)("Edit")," ",Object(C.f)("strong",null,this.props.language)," ",Object(u.e)("in modal")),modalBody:this.renderModalBody(!0),responsive:!0}))}}j.propTypes=O,j.defaultProps={onChange:()=>{},value:"",height:250,minLines:3,maxLines:10,offerEditInModal:!0,readOnly:!1}},982:function(e,t,n){"use strict";var o=n(8),a=n.n(o),s=(n(0),n(2)),r=n.n(s),l=n(14),i=n(634),c=n(83),h=n(114),p=n(1);const d={dataEndpoint:r.a.string.isRequired,multi:r.a.bool,mutator:r.a.func,onAsyncErrorMessage:r.a.string,onChange:r.a.func,placeholder:r.a.string,value:r.a.oneOfType([r.a.string,r.a.number,r.a.arrayOf(r.a.string),r.a.arrayOf(r.a.number)]),addDangerToast:r.a.func.isRequired},u={multi:!0,onAsyncErrorMessage:Object(l.e)("Error while fetching data"),onChange:()=>{},placeholder:Object(l.e)("Select ...")},b=e=>{const{value:t,onChange:n,dataEndpoint:o,multi:s,mutator:r,placeholder:l,onAsyncErrorMessage:h}=e;return Object(p.f)("div",null,Object(p.f)(c.a,e),Object(p.f)(i.a,{dataEndpoint:o,onChange:e=>{let t;var o,r;s?t=null!=(o=null==e?void 0:a()(e).call(e,e=>e.value))?o:null:t=null!=(r=null==e?void 0:e.value)?r:null;n(t)},onAsyncError:t=>e.addDangerToast(`${h}: ${t}`),mutator:r,multi:s,value:t,placeholder:l,valueRenderer:e=>Object(p.f)("div",null,e.label)}))};b.propTypes=d,b.defaultProps=u,t.a=Object(h.a)(b)},984:function(e,t,n){"use strict";n.d(t,"a",(function(){return x}));var o=n(9),a=n.n(o),s=n(0),r=n.n(s),l=n(2),i=n.n(l),c=n(1082),h=n(908),p=n(14),d=n(107),u=n(22).q,b=n(342),f=n(638),g=n(83),m=n(389),v=n(1);const C="latlong",O="delimited",j="geohash",y={onChange:i.a.func,value:i.a.object,animation:i.a.bool,choices:i.a.array};class x extends r.a.Component{constructor(e){var t,n,o;super(e);const s=e.value||{};let r;e.choices.length>0&&(r=e.choices[0][0]),this.state={type:s.type||C,delimiter:s.delimiter||",",latCol:s.latCol||r,lonCol:s.lonCol||r,lonlatCol:s.lonlatCol||r,reverseCheckbox:s.reverseCheckbox||!1,geohashCol:s.geohashCol||r,value:null,errors:[]},this.toggleCheckbox=a()(t=this.toggleCheckbox).call(t,this),this.onChange=a()(n=this.onChange).call(n,this),this.renderReverseCheckbox=a()(o=this.renderReverseCheckbox).call(o,this)}componentDidMount(){this.onChange()}onChange(){const{type:e}=this.state,t={type:e},n=[],o=Object(p.e)("Invalid lat/long configuration.");e===C?(t.latCol=this.state.latCol,t.lonCol=this.state.lonCol,t.lonCol&&t.latCol||n.push(o)):e===O?(t.lonlatCol=this.state.lonlatCol,t.delimiter=this.state.delimiter,t.reverseCheckbox=this.state.reverseCheckbox,t.lonlatCol&&t.delimiter||n.push(o)):e===j&&(t.geohashCol=this.state.geohashCol,t.reverseCheckbox=this.state.reverseCheckbox,t.geohashCol||n.push(o)),this.setState({value:t,errors:n}),this.props.onChange(t,n)}setType(e){this.setState({type:e},this.onChange)}toggleCheckbox(){this.setState(e=>({reverseCheckbox:!e.reverseCheckbox}),this.onChange)}renderLabelContent(){return this.state.errors.length>0?"N/A":this.state.type===C?`${this.state.lonCol} | ${this.state.latCol}`:this.state.type===O?`${this.state.lonlatCol}`:this.state.type===j?`${this.state.geohashCol}`:null}renderSelect(e,t){return Object(v.f)(m.a,{name:e,choices:this.props.choices,value:this.state[e],clearable:!1,onFocus:()=>{this.setType(t)},onChange:t=>{this.setState({[e]:t},this.onChange)}})}renderReverseCheckbox(){return Object(v.f)("span",null,Object(p.e)("Reverse lat/long "),Object(v.f)(f.a,{checked:this.state.reverseCheckbox,onChange:this.toggleCheckbox}))}renderPopoverContent(){var e,t,n;return Object(v.f)("div",{style:{width:"300px"}},Object(v.f)(b.a,{title:Object(p.e)("Longitude & Latitude columns"),isSelected:this.state.type===C,onSelect:a()(e=this.setType).call(e,this,C)},Object(v.f)(c.a,null,Object(v.f)(h.a,{md:6},"Longitude",this.renderSelect("lonCol",C)),Object(v.f)(h.a,{md:6},"Latitude",this.renderSelect("latCol",C)))),Object(v.f)(b.a,{title:Object(p.e)("Delimited long & lat single column"),info:Object(p.e)("Multiple formats accepted, look the geopy.points Python library for more details"),isSelected:this.state.type===O,onSelect:a()(t=this.setType).call(t,this,O)},Object(v.f)(c.a,null,Object(v.f)(h.a,{md:6},Object(p.e)("Column"),this.renderSelect("lonlatCol",O)),Object(v.f)(h.a,{md:6},this.renderReverseCheckbox()))),Object(v.f)(b.a,{title:Object(p.e)("Geohash"),isSelected:this.state.type===j,onSelect:a()(n=this.setType).call(n,this,j)},Object(v.f)(c.a,null,Object(v.f)(h.a,{md:6},"Column",this.renderSelect("geohashCol",j)),Object(v.f)(h.a,{md:6},this.renderReverseCheckbox()))))}render(){return Object(v.f)("div",null,Object(v.f)(g.a,this.props),Object(v.f)(u,{content:this.renderPopoverContent(),placement:"topLeft",trigger:"click"},Object(v.f)(d.a,{className:"pointer"},this.renderLabelContent())))}}x.propTypes=y,x.defaultProps={onChange:()=>{},animation:!0,choices:[]}}}]);