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
	import NavigationMobile from '$lib/NavigationMobile.svelte';

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
	<NavigationMobile />
</Drawer>

<AppShell>
	<svelte:fragment slot="header">
		<Navigation />
	</svelte:fragment>
	<slot />
</AppShell>
