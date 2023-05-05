<template>
    <router-view></router-view>
</template>

<script>
export default {

}
</script>

<style>
* {
    padding: 0;
    margin: 0;
    border: 0;
}

*,
*:before,
*:after {
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
}

:focus,
:active {
    outline: none;
}

a:focus,
a:active {
    outline: none;
}

nav,
footer,
header,
aside {
    display: block;
}

html,
body {
    height: 100%;
    width: 100%;
    font-size: 100%;
    line-height: 1;
    font-size: 14px;
    -ms-text-size-adjust: 100%;
    -moz-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
}

input,
button,
textarea {
    font-family: inherit;
}

input::-ms-clear {
    display: none;
}

button {
    cursor: pointer;
    background: transparent;
}

button::-moz-focus-inner {
    padding: 0;
    border: 0;
}

a,
a:visited {
    text-decoration: none;
}

a:hover {
    text-decoration: none;
}

ul li {
    list-style: none;
}

img {
    vertical-align: top;
}

h1,
h2,
h3,
h4,
h5,
h6 {
    font-size: inherit;
    font-weight: inherit;
}

* {
    font-family: 'Montserrat', sans-serif;
}


a {
    color: black;
}

a:visited {
    color: black;
}

a:hover {
    color: rgba(128, 0, 128, 0.5);
}

button:hover {
    color: rgba(128, 0, 128, 0.5);
}

#app {
    /* height: 100%; */
    width: 65%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

}
</style>