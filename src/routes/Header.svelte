<script>
	import { page } from "$app/stores";
	import logo from "$lib/images/svelte-logo.svg";
	import github from "$lib/images/github.svg";
</script>

<header>
	<div class="corner">
		<a href="/">RNNLA DASHBOARD</a>
	</div>

	<div class="corner">
		<a href="https://github.com/RNNLA">
			<img src={github} alt="GitHub" />
		</a>
	</div>
</header>

<style>
	header {
		display: flex;
		justify-content: space-between;
		background-color: #33363f;
		height: 10%;
	}

	.corner {
		padding: 1em;
	}

	.corner a {
		font-size: large;
		font-weight: 700;
		height: 100%;
		display: flex;
		align-items: center;
		color: white;
	}

	.corner img {
		width: 2em;
		height: 2em;
	}

	a:hover {
		color: var(--color-theme-1);
	}
</style>
