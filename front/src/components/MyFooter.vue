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
	border-top-right-radius: 20px;
	border-top-left-radius: 20px;
	align-items: center;
	justify-content: center;
	font-size: 1.3rem;
	height: 100px;
	width: 100%;
	background-color: rgb(0, 0, 0);
	color: white;

	p {
		border-bottom: 2px solid rgb(255, 176, 251);
	}
}
</style>