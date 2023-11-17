<script lang="ts">
	import { BlockLabel } from "@gradio/atoms";
	import { Image } from "@gradio/icons";
	import type { I18nFormatter } from "@gradio/utils";
	import { ImagePaste, Upload as UploadIcon } from "@gradio/icons";
	import { Toolbar, IconButton } from "@gradio/atoms";

	import { Upload } from "@gradio/upload";
	import { type FileData, normalise_file } from "@gradio/client";
	import ClearImage from "./ClearImage.svelte";
	import SveltePannellum from './SveltePannellum.svelte';

	export let value: null | FileData;
	export let label: string | undefined = undefined;
	export let height: number = 400;
	export let show_label: boolean;

	export let sources: ("clipboard" | "upload")[] = ["upload", "clipboard"];
	export let root: string;
	export let i18n: I18nFormatter;

	let upload: Upload;

	function handle_upload({ detail }: CustomEvent<FileData>): void {
		value = normalise_file(detail, root, null);
	}

	$: value && !value.url && (value = normalise_file(value, root, null));

	let dragging = false;

	const sources_meta = {
		upload: {
			icon: UploadIcon,
			label: i18n("Upload"),
			order: 0
		},
		clipboard: {
			icon: ImagePaste,
			label: i18n("Paste"),
			order: 1
		}
	};

	$: sources_list = sources.sort(
		(a, b) => sources_meta[a].order - sources_meta[b].order
	);

	async function handle_toolbar(
		source: (typeof sources)[number]
	): Promise<void> {
		switch (source) {
			case "clipboard":
				navigator.clipboard.read().then(async (items) => {
					for (let i = 0; i < items.length; i++) {
						const type = items[i].types.find((t) => t.startsWith("image/"));
						if (type) {
							items[i].getType(type).then(async (blob) => {
								const f = await upload.load_files([
									new File([blob], `clipboard.${type.replace("image/", "")}`)
								]);
								f;
								value = f?.[0] || null;
							});
							break;
						}
					}
				});
				break;
			case "upload":
				upload.open_file_upload();
				break;
			default:
				break;
		}
	}
</script>

<BlockLabel {show_label} Icon={Image} label={label || "Image"} />

<div data-testid="image" class="image-container">
	{#if value?.url}
		<ClearImage on:remove_image={() => (value = null)} />
	{/if}
	<div class="upload-container">
		<Upload
			hidden={value !== null}
			bind:this={upload}
			bind:dragging
			filetype="image/*"
			on:load={handle_upload}
			on:error
			{root}
			disable_click={!sources.includes("upload")}
		>
			{#if value === null}
				<slot />
			{/if}
		</Upload>
		{#if value !== null}
			<!-- svelte-ignore a11y-click-events-have-key-events-->
			<!-- svelte-ignore a11y-no-noninteractive-element-interactions-->
			<SveltePannellum div_id="pannellum-uploader-{value.orig_name}" panorama={value.url} height={height}/>
		{/if}
	</div>
	{#if sources.length > 1 || sources.includes("clipboard")}
		<Toolbar show_border={!value?.url}>
			{#each sources_list as source}
				<IconButton
					on:click={() => handle_toolbar(source)}
					Icon={sources_meta[source].icon}
					size="large"
					padded={false}
				/>
			{/each}
		</Toolbar>
	{/if}
</div>

<style>
	.upload-container {
		height: 100%;
		flex-shrink: 1;
		max-height: 100%;
		width: 100%;
	}

	.image-container {
		display: flex;
		height: 100%;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		max-height: 100%;
	}
</style>
