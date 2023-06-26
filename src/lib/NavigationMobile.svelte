<script lang="ts">
	import { goto } from '$app/navigation';
	import { AppRailTile, drawerStore } from '@skeletonlabs/skeleton';

	function drawerClose(): void {
		drawerStore.close();
	}

	function about() {
		goto('/about');
		drawerClose();
	}

	function map() {
		goto('/map');
		drawerClose();
	}
</script>

<div class=" h-full flex justify-center items-center">
	<div class="grid grid-cols-1 gap-3 text-2xl">
		<AppRailTile on:click={map}
			><div class="flex place-items-center flex-col">
				<span class="material-symbols-outlined"> map </span>
				<h3 class="h3">Map</h3>
			</div></AppRailTile
		>
		<AppRailTile on:click={about}
			><div class="flex place-items-center flex-col">
				<span class="material-symbols-outlined"> book </span>
				<h3 class="h3">About</h3>
			</div></AppRailTile
		>
		<AppRailTile on:click={() => goto('https://github.com/jjoeldaniel/disease_visual')}
			><div class="flex place-items-center flex-col">
				<span class="material-symbols-outlined"> trophy </span>
				<h3 class="h3">Source Code</h3>
			</div></AppRailTile
		>
	</div>
</div>
