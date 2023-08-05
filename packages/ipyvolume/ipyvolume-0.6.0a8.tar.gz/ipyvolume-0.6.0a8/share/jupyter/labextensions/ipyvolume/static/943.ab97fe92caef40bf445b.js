(self.webpackChunkipyvolume=self.webpackChunkipyvolume||[]).push([[943],{6239:(r,e,n)=>{"use strict";var a=n(5081);function s(){this.argTypes=[],this.shimArgs=[],this.arrayArgs=[],this.arrayBlockIndices=[],this.scalarArgs=[],this.offsetArgs=[],this.offsetArgIndex=[],this.indexArgs=[],this.shapeArgs=[],this.funcName="",this.pre=null,this.body=null,this.post=null,this.debug=!1}r.exports=function(r){var e=new s;e.pre=r.pre,e.body=r.body,e.post=r.post;var n=r.args.slice(0);e.argTypes=n;for(var o=0;o<n.length;++o){var i=n[o];if("array"===i||"object"==typeof i&&i.blockIndices){if(e.argTypes[o]="array",e.arrayArgs.push(o),e.arrayBlockIndices.push(i.blockIndices?i.blockIndices:0),e.shimArgs.push("array"+o),o<e.pre.args.length&&e.pre.args[o].count>0)throw new Error("cwise: pre() block may not reference array args");if(o<e.post.args.length&&e.post.args[o].count>0)throw new Error("cwise: post() block may not reference array args")}else if("scalar"===i)e.scalarArgs.push(o),e.shimArgs.push("scalar"+o);else if("index"===i){if(e.indexArgs.push(o),o<e.pre.args.length&&e.pre.args[o].count>0)throw new Error("cwise: pre() block may not reference array index");if(o<e.body.args.length&&e.body.args[o].lvalue)throw new Error("cwise: body() block may not write to array index");if(o<e.post.args.length&&e.post.args[o].count>0)throw new Error("cwise: post() block may not reference array index")}else if("shape"===i){if(e.shapeArgs.push(o),o<e.pre.args.length&&e.pre.args[o].lvalue)throw new Error("cwise: pre() block may not write to array shape");if(o<e.body.args.length&&e.body.args[o].lvalue)throw new Error("cwise: body() block may not write to array shape");if(o<e.post.args.length&&e.post.args[o].lvalue)throw new Error("cwise: post() block may not write to array shape")}else{if("object"!=typeof i||!i.offset)throw new Error("cwise: Unknown argument type "+n[o]);e.argTypes[o]="offset",e.offsetArgs.push({array:i.array,offset:i.offset}),e.offsetArgIndex.push(o)}}if(e.arrayArgs.length<=0)throw new Error("cwise: No array arguments specified");if(e.pre.args.length>n.length)throw new Error("cwise: Too many arguments in pre() block");if(e.body.args.length>n.length)throw new Error("cwise: Too many arguments in body() block");if(e.post.args.length>n.length)throw new Error("cwise: Too many arguments in post() block");return e.debug=!!r.printCode||!!r.debug,e.funcName=r.funcName||"cwise",e.blockSize=r.blockSize||64,a(e)}},1984:(r,e,n)=>{"use strict";var a=n(3319);function s(r,e,n){var a,s,o=r.length,i=e.arrayArgs.length,t=e.indexArgs.length>0,h=[],p=[],l=0,c=0;for(a=0;a<o;++a)p.push(["i",a,"=0"].join(""));for(s=0;s<i;++s)for(a=0;a<o;++a)c=l,l=r[a],0===a?p.push(["d",s,"s",a,"=t",s,"p",l].join("")):p.push(["d",s,"s",a,"=(t",s,"p",l,"-s",c,"*t",s,"p",c,")"].join(""));for(p.length>0&&h.push("var "+p.join(",")),a=o-1;a>=0;--a)l=r[a],h.push(["for(i",a,"=0;i",a,"<s",l,";++i",a,"){"].join(""));for(h.push(n),a=0;a<o;++a){for(c=l,l=r[a],s=0;s<i;++s)h.push(["p",s,"+=d",s,"s",a].join(""));t&&(a>0&&h.push(["index[",c,"]-=s",c].join("")),h.push(["++index[",l,"]"].join(""))),h.push("}")}return h.join("\n")}function o(r,e,n){for(var a=r.body,s=[],o=[],i=0;i<r.args.length;++i){var t=r.args[i];if(!(t.count<=0)){var h=new RegExp(t.name,"g"),p="",l=e.arrayArgs.indexOf(i);switch(e.argTypes[i]){case"offset":var c=e.offsetArgIndex.indexOf(i);l=e.offsetArgs[c].array,p="+q"+c;case"array":p="p"+l+p;var u="l"+i,g="a"+l;if(0===e.arrayBlockIndices[l])1===t.count?"generic"===n[l]?t.lvalue?(s.push(["var ",u,"=",g,".get(",p,")"].join("")),a=a.replace(h,u),o.push([g,".set(",p,",",u,")"].join(""))):a=a.replace(h,[g,".get(",p,")"].join("")):a=a.replace(h,[g,"[",p,"]"].join("")):"generic"===n[l]?(s.push(["var ",u,"=",g,".get(",p,")"].join("")),a=a.replace(h,u),t.lvalue&&o.push([g,".set(",p,",",u,")"].join(""))):(s.push(["var ",u,"=",g,"[",p,"]"].join("")),a=a.replace(h,u),t.lvalue&&o.push([g,"[",p,"]=",u].join("")));else{for(var f=[t.name],y=[p],d=0;d<Math.abs(e.arrayBlockIndices[l]);d++)f.push("\\s*\\[([^\\]]+)\\]"),y.push("$"+(d+1)+"*t"+l+"b"+d);if(h=new RegExp(f.join(""),"g"),p=y.join("+"),"generic"===n[l])throw new Error("cwise: Generic arrays not supported in combination with blocks!");a=a.replace(h,[g,"[",p,"]"].join(""))}break;case"scalar":a=a.replace(h,"Y"+e.scalarArgs.indexOf(i));break;case"index":a=a.replace(h,"index");break;case"shape":a=a.replace(h,"shape")}}}return[s.join("\n"),a,o.join("\n")].join("\n").trim()}function i(r){for(var e=new Array(r.length),n=!0,a=0;a<r.length;++a){var s=r[a],o=s.match(/\d+/);o=o?o[0]:"",0===s.charAt(0)?e[a]="u"+s.charAt(1)+o:e[a]=s.charAt(0)+o,a>0&&(n=n&&e[a]===e[a-1])}return n?e[0]:e.join("")}r.exports=function(r,e){for(var n=e[1].length-Math.abs(r.arrayBlockIndices[0])|0,t=new Array(r.arrayArgs.length),h=new Array(r.arrayArgs.length),p=0;p<r.arrayArgs.length;++p)h[p]=e[2*p],t[p]=e[2*p+1];var l=[],c=[],u=[],g=[],f=[];for(p=0;p<r.arrayArgs.length;++p){r.arrayBlockIndices[p]<0?(u.push(0),g.push(n),l.push(n),c.push(n+r.arrayBlockIndices[p])):(u.push(r.arrayBlockIndices[p]),g.push(r.arrayBlockIndices[p]+n),l.push(0),c.push(r.arrayBlockIndices[p]));for(var y=[],d=0;d<t[p].length;d++)u[p]<=t[p][d]&&t[p][d]<g[p]&&y.push(t[p][d]-u[p]);f.push(y)}var j=["SS"],_=["'use strict'"],v=[];for(d=0;d<n;++d)v.push(["s",d,"=SS[",d,"]"].join(""));for(p=0;p<r.arrayArgs.length;++p){for(j.push("a"+p),j.push("t"+p),j.push("p"+p),d=0;d<n;++d)v.push(["t",p,"p",d,"=t",p,"[",u[p]+d,"]"].join(""));for(d=0;d<Math.abs(r.arrayBlockIndices[p]);++d)v.push(["t",p,"b",d,"=t",p,"[",l[p]+d,"]"].join(""))}for(p=0;p<r.scalarArgs.length;++p)j.push("Y"+p);if(r.shapeArgs.length>0&&v.push("shape=SS.slice(0)"),r.indexArgs.length>0){var w=new Array(n);for(p=0;p<n;++p)w[p]="0";v.push(["index=[",w.join(","),"]"].join(""))}for(p=0;p<r.offsetArgs.length;++p){var b=r.offsetArgs[p],A=[];for(d=0;d<b.offset.length;++d)0!==b.offset[d]&&(1===b.offset[d]?A.push(["t",b.array,"p",d].join("")):A.push([b.offset[d],"*t",b.array,"p",d].join("")));0===A.length?v.push("q"+p+"=0"):v.push(["q",p,"=",A.join("+")].join(""))}var k=a([].concat(r.pre.thisVars).concat(r.body.thisVars).concat(r.post.thisVars));for((v=v.concat(k)).length>0&&_.push("var "+v.join(",")),p=0;p<r.arrayArgs.length;++p)_.push("p"+p+"|=0");r.pre.body.length>3&&_.push(o(r.pre,r,h));var m=o(r.body,r,h),x=function(r){for(var e=0,n=r[0].length;e<n;){for(var a=1;a<r.length;++a)if(r[a][e]!==r[0][e])return e;++e}return e}(f);x<n?_.push(function(r,e,n,a){for(var o=e.length,i=n.arrayArgs.length,t=n.blockSize,h=n.indexArgs.length>0,p=[],l=0;l<i;++l)p.push(["var offset",l,"=p",l].join(""));for(l=r;l<o;++l)p.push(["for(var j"+l+"=SS[",e[l],"]|0;j",l,">0;){"].join("")),p.push(["if(j",l,"<",t,"){"].join("")),p.push(["s",e[l],"=j",l].join("")),p.push(["j",l,"=0"].join("")),p.push(["}else{s",e[l],"=",t].join("")),p.push(["j",l,"-=",t,"}"].join("")),h&&p.push(["index[",e[l],"]=j",l].join(""));for(l=0;l<i;++l){for(var c=["offset"+l],u=r;u<o;++u)c.push(["j",u,"*t",l,"p",e[u]].join(""));p.push(["p",l,"=(",c.join("+"),")"].join(""))}for(p.push(s(e,n,a)),l=r;l<o;++l)p.push("}");return p.join("\n")}(x,f[0],r,m)):_.push(s(f[0],r,m)),r.post.body.length>3&&_.push(o(r.post,r,h)),r.debug&&console.log("-----Generated cwise routine for ",e,":\n"+_.join("\n")+"\n----------");var I=[r.funcName||"unnamed","_cwise_loop_",t[0].join("s"),"m",x,i(h)].join("");return new Function(["function ",I,"(",j.join(","),"){",_.join("\n"),"} return ",I].join(""))()}},5081:(r,e,n)=>{"use strict";var a=n(1984);r.exports=function(r){var e=["'use strict'","var CACHED={}"],n=[],s=r.funcName+"_cwise_thunk";e.push(["return function ",s,"(",r.shimArgs.join(","),"){"].join(""));for(var o=[],i=[],t=[["array",r.arrayArgs[0],".shape.slice(",Math.max(0,r.arrayBlockIndices[0]),r.arrayBlockIndices[0]<0?","+r.arrayBlockIndices[0]+")":")"].join("")],h=[],p=[],l=0;l<r.arrayArgs.length;++l){var c=r.arrayArgs[l];n.push(["t",c,"=array",c,".dtype,","r",c,"=array",c,".order"].join("")),o.push("t"+c),o.push("r"+c),i.push("t"+c),i.push("r"+c+".join()"),t.push("array"+c+".data"),t.push("array"+c+".stride"),t.push("array"+c+".offset|0"),l>0&&(h.push("array"+r.arrayArgs[0]+".shape.length===array"+c+".shape.length+"+(Math.abs(r.arrayBlockIndices[0])-Math.abs(r.arrayBlockIndices[l]))),p.push("array"+r.arrayArgs[0]+".shape[shapeIndex+"+Math.max(0,r.arrayBlockIndices[0])+"]===array"+c+".shape[shapeIndex+"+Math.max(0,r.arrayBlockIndices[l])+"]"))}for(r.arrayArgs.length>1&&(e.push("if (!("+h.join(" && ")+")) throw new Error('cwise: Arrays do not all have the same dimensionality!')"),e.push("for(var shapeIndex=array"+r.arrayArgs[0]+".shape.length-"+Math.abs(r.arrayBlockIndices[0])+"; shapeIndex--\x3e0;) {"),e.push("if (!("+p.join(" && ")+")) throw new Error('cwise: Arrays do not all have the same shape!')"),e.push("}")),l=0;l<r.scalarArgs.length;++l)t.push("scalar"+r.scalarArgs[l]);return n.push(["type=[",i.join(","),"].join()"].join("")),n.push("proc=CACHED[type]"),e.push("var "+n.join(",")),e.push(["if(!proc){","CACHED[type]=proc=compile([",o.join(","),"])}","return proc(",t.join(","),")}"].join("")),r.debug&&console.log("-----Generated thunk:\n"+e.join("\n")+"\n----------"),new Function("compile",e.join("\n"))(a.bind(void 0,r))}},1943:(r,e,n)=>{"use strict";var a=n(3936),s=n(1895);r.exports=function(r,e){for(var n=[],o=r,i=1;Array.isArray(o);)n.push(o.length),i*=o.length,o=o[0];return 0===n.length?a():(e||(e=a(new Float64Array(i),n)),s(e,r),e)}},1895:(r,e,n)=>{r.exports=n(6239)({args:["array","scalar","index"],pre:{body:"{}",args:[],thisVars:[],localVars:[]},body:{body:"{\nvar _inline_1_v=_inline_1_arg1_,_inline_1_i\nfor(_inline_1_i=0;_inline_1_i<_inline_1_arg2_.length-1;++_inline_1_i) {\n_inline_1_v=_inline_1_v[_inline_1_arg2_[_inline_1_i]]\n}\n_inline_1_arg0_=_inline_1_v[_inline_1_arg2_[_inline_1_arg2_.length-1]]\n}",args:[{name:"_inline_1_arg0_",lvalue:!0,rvalue:!1,count:1},{name:"_inline_1_arg1_",lvalue:!1,rvalue:!0,count:1},{name:"_inline_1_arg2_",lvalue:!1,rvalue:!0,count:4}],thisVars:[],localVars:["_inline_1_i","_inline_1_v"]},post:{body:"{}",args:[],thisVars:[],localVars:[]},funcName:"convert",blockSize:64})},3319:r=>{"use strict";r.exports=function(r,e,n){return 0===r.length?r:e?(n||r.sort(e),function(r,e){for(var n=1,a=r.length,s=r[0],o=r[0],i=1;i<a;++i)if(o=s,e(s=r[i],o)){if(i===n){n++;continue}r[n++]=s}return r.length=n,r}(r,e)):(n||r.sort(),function(r){for(var e=1,n=r.length,a=r[0],s=r[0],o=1;o<n;++o,s=a)if(s=a,(a=r[o])!==s){if(o===e){e++;continue}r[e++]=a}return r.length=e,r}(r))}}}]);