<template>
	<footer class="footer">
		<p>NicePC All rights reserved &copy;</p>
	</footer>
</template>

<script>
export default {

}

</script>

<style lang="scss" scoped>
.footer {
	display: flex;

	align-items: center;
	justify-content: center;
	font-size: 1.3rem;
	height: 50px;
	width: 100%;
	background-color: rgb(21, 21, 21);
	color: rgb(240, 240, 240);
	position: fixed;
	bottom: 0;
	left: 0;
	z-index: 3;
	p {
		border-bottom: 2px solid rgb(255, 176, 251);
	}
}
</style>