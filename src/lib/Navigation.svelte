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
</script>

<div class=" h-full flex justify-center items-center">
	<div class="grid grid-cols-1 gap-3 text-2xl">
		<AppRailTile on:click={about}
			><div class="flex place-items-center flex-col">
				<span class="material-symbols-outlined"> book </span>
				About
			</div></AppRailTile
		>
		<AppRailTile on:click={() => goto('https://github.com/jjoeldaniel/disease_visual')}
			><div class="flex place-items-center flex-col">
				<span class="material-symbols-outlined"> trophy </span>
				Source Code
			</div></AppRailTile
		>
	</div>
</div>
