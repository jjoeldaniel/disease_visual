<script lang="ts">
	// The ordering of these imports is critical to your app working properly
	import '@skeletonlabs/skeleton/themes/theme-rocket.css';
	// If you have source.organizeImports set to true in VSCode, then it will auto change this ordering
	import '@skeletonlabs/skeleton/styles/skeleton.css';
	// Most of your app wide CSS should be put in this file
	import '../app.postcss';

	import { AppShell, AppBar, LightSwitch } from '@skeletonlabs/skeleton';
	import { Drawer, drawerStore } from '@skeletonlabs/skeleton';
	import { TabGroup, Tab } from '@skeletonlabs/skeleton';

	import Navigation from '$lib/Navigation.svelte';

	import { page } from '$app/stores';
	import { goto } from '$app/navigation';

	function drawerOpen(): void {
		drawerStore.open({
			position: 'top'
		});
	}

	let tabsBottomNav = 0;
	let path = $page.url.pathname;
	switch (path) {
		case '/':
			tabsBottomNav = 0;
			break;
		case '/blog':
			tabsBottomNav = 1;
			break;
		case '/projects':
			tabsBottomNav = 2;
			break;
		case '/contact':
			tabsBottomNav = 3;
			break;
		default:
			tabsBottomNav = 0;
	}

	function buttonClick(event: MouseEvent): void {
		let targetPath = event.target.name;
		goto(targetPath);
	}
</script>

<link
	rel="stylesheet"
	href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
/>

<Drawer>
	<Navigation />
</Drawer>

<AppShell>
	<svelte:fragment slot="header">
		<AppBar
			padding="pt-2 pb-2 md:pt-0 md:pb-0"
			gridColumns="grid-cols-3"
			slotDefault="place-self-center"
			slotTrail="place-content-end"
		>
			<svelte:fragment slot="lead"
				><button class="btn btn-sm mr-4 block lg:hidden" on:click={drawerOpen}>
					<span>
						<svg viewBox="0 0 100 80" class="fill-token w-4 h-4">
							<rect width="100" height="20" />
							<rect y="30" width="100" height="20" />
							<rect y="60" width="100" height="20" />
						</svg>
					</span>
				</button>
				<div class="hidden lg:block">
					<TabGroup
						justify="justify-center"
						active="variant-filled-primary"
						hover="hover:variant-soft-primary"
						flex="flex-1 lg:flex-none"
						rounded=""
						border=""
						class="bg-surface-100-800-token w-full"
					>
						<Tab on:click={buttonClick} bind:group={tabsBottomNav} name="home" value={0}>
							<svelte:fragment slot="lead"
								><span class="material-symbols-outlined"> home </span></svelte:fragment
							>
							Home
						</Tab>
						<Tab on:click={buttonClick} bind:group={tabsBottomNav} name="about" value={1}>
							<svelte:fragment slot="lead"
								><span class="material-symbols-outlined"> article </span></svelte:fragment
							>
							About
						</Tab>
						<Tab
							on:click={() => goto('https://github.com/jjoeldaniel/disease_visual')}
							bind:group={tabsBottomNav}
							name="projects"
							value={2}
						>
							<svelte:fragment slot="lead"
								><span class="material-symbols-outlined"> trophy </span></svelte:fragment
							>
							Source Code
						</Tab>
					</TabGroup>
				</div>
			</svelte:fragment>
			<h4 class="h4 font-bold gradient-heading"><a href="/">Disease Visualizer</a></h4>
			<svelte:fragment slot="trail"
				><div class="pr-3">
					<LightSwitch />
				</div></svelte:fragment
			>
		</AppBar>
	</svelte:fragment>
	<slot />
</AppShell>
