(function(){"use strict";var t={2436:function(t,n,o){var e=o(9242),r=o(3396);const s={class:"app"};function u(t,n,o,e,u,i){const a=(0,r.up)("post-form"),c=(0,r.up)("post-list");return(0,r.wg)(),(0,r.iD)("div",s,[(0,r.Wm)(a,{posts:u.posts,onCreate:i.createPost},null,8,["posts","onCreate"]),(0,r.Wm)(c,{posts:u.posts},null,8,["posts"])])}o(7658);const i=t=>((0,r.dD)("data-v-2d81c4fa"),t=t(),(0,r.Cn)(),t),a=i((()=>(0,r._)("h4",null,"Создание поста",-1)));function c(t,n,o,s,u,i){const c=(0,r.up)("my-button");return(0,r.wg)(),(0,r.iD)("form",{onSubmit:n[2]||(n[2]=(0,e.iM)((()=>{}),["prevent"]))},[a,(0,r.wy)((0,r._)("input",{"onUpdate:modelValue":n[0]||(n[0]=t=>u.post.title=t),class:"input",type:"text",placeholder:"Название"},null,512),[[e.nr,u.post.title]]),(0,r.wy)((0,r._)("input",{"onUpdate:modelValue":n[1]||(n[1]=t=>u.post.body=t),class:"input",type:"text",placeholder:"Описание"},null,512),[[e.nr,u.post.body]]),(0,r.Wm)(c,{class:"btn",style:{"align-self":"flex-end"},onClick:i.createPost},{default:(0,r.w5)((()=>[(0,r.Uk)(" Создать ")])),_:1},8,["onClick"])],32)}var l={data(){return{post:{title:"",body:""}}},methods:{createPost(){this.post.id=Date.now(),this.$emit("create",this.post),this.post={title:"",body:""}}}},p=o(89);const d=(0,p.Z)(l,[["render",c],["__scopeId","data-v-2d81c4fa"]]);var f=d;const v=(0,r._)("h3",null,"List of users",-1);function b(t,n,o,e,s,u){const i=(0,r.up)("post-item");return(0,r.wg)(),(0,r.iD)("div",null,[v,((0,r.wg)(!0),(0,r.iD)(r.HY,null,(0,r.Ko)(o.posts,(t=>((0,r.wg)(),(0,r.j4)(i,{post:t},null,8,["post"])))),256))])}var h=o(7139);const m=t=>((0,r.dD)("data-v-9363bad2"),t=t(),(0,r.Cn)(),t),w={class:"post"},y=m((()=>(0,r._)("strong",null,"Название:",-1))),_=m((()=>(0,r._)("strong",null,"Описание:",-1))),g={class:"post_btns"};function O(t,n,o,e,s,u){const i=(0,r.up)("my-button");return(0,r.wg)(),(0,r.iD)("div",w,[(0,r._)("div",null,[(0,r._)("div",null,[y,(0,r.Uk)(" "+(0,h.zw)(o.post.title),1)]),(0,r._)("div",null,[_,(0,r.Uk)(" "+(0,h.zw)(o.post.body),1)])]),(0,r._)("div",g,[(0,r.Wm)(i,null,{default:(0,r.w5)((()=>[(0,r.Uk)("Delete")])),_:1})])])}var k={props:{post:{type:Object,required:!0}}};const D=(0,p.Z)(k,[["render",O],["__scopeId","data-v-9363bad2"]]);var P=D,j={components:{PostItem:P},props:{posts:{type:Array,required:!0}}};const C=(0,p.Z)(j,[["render",b]]);var x=C,U={components:{PostList:x,PostForm:f},data(){return{posts:[]}},methods:{createPost(t){this.posts.push(t)}}};const I=(0,p.Z)(U,[["render",u]]);var W=I;const Z={class:"btn"};function q(t,n,o,e,s,u){return(0,r.wg)(),(0,r.iD)("button",Z,[(0,r.WI)(t.$slots,"default",{},void 0,!0)])}var z={name:"my-button"};const E=(0,p.Z)(z,[["render",q],["__scopeId","data-v-c4f9db50"]]);var F=E,L=[F];const M=(0,e.ri)(W);L.forEach((t=>{M.component(t.name,t)})),M.mount("#app")}},n={};function o(e){var r=n[e];if(void 0!==r)return r.exports;var s=n[e]={exports:{}};return t[e](s,s.exports,o),s.exports}o.m=t,function(){var t=[];o.O=function(n,e,r,s){if(!e){var u=1/0;for(l=0;l<t.length;l++){e=t[l][0],r=t[l][1],s=t[l][2];for(var i=!0,a=0;a<e.length;a++)(!1&s||u>=s)&&Object.keys(o.O).every((function(t){return o.O[t](e[a])}))?e.splice(a--,1):(i=!1,s<u&&(u=s));if(i){t.splice(l--,1);var c=r();void 0!==c&&(n=c)}}return n}s=s||0;for(var l=t.length;l>0&&t[l-1][2]>s;l--)t[l]=t[l-1];t[l]=[e,r,s]}}(),function(){o.n=function(t){var n=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(n,{a:n}),n}}(),function(){o.d=function(t,n){for(var e in n)o.o(n,e)&&!o.o(t,e)&&Object.defineProperty(t,e,{enumerable:!0,get:n[e]})}}(),function(){o.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){o.o=function(t,n){return Object.prototype.hasOwnProperty.call(t,n)}}(),function(){var t={143:0};o.O.j=function(n){return 0===t[n]};var n=function(n,e){var r,s,u=e[0],i=e[1],a=e[2],c=0;if(u.some((function(n){return 0!==t[n]}))){for(r in i)o.o(i,r)&&(o.m[r]=i[r]);if(a)var l=a(o)}for(n&&n(e);c<u.length;c++)s=u[c],o.o(t,s)&&t[s]&&t[s][0](),t[s]=0;return o.O(l)},e=self["webpackChunkweb"]=self["webpackChunkweb"]||[];e.forEach(n.bind(null,0)),e.push=n.bind(null,e.push.bind(e))}();var e=o.O(void 0,[998],(function(){return o(2436)}));e=o.O(e)})();
//# sourceMappingURL=app.7907c72b.js.map