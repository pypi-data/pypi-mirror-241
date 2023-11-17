<script lang="ts">
	import { uploadToHuggingFace } from "@gradio/utils";
	import { BlockLabel, Empty, IconButton, ShareButton } from "@gradio/atoms";
	import { Download } from "@gradio/icons";

	import { Image } from "@gradio/icons";
	import { type FileData } from "@gradio/client";
	import type { I18nFormatter } from "@gradio/utils";
	import SveltePannellum from './SveltePannellum.svelte';

	export let value: null | FileData;
	export let label: string | undefined = undefined;
	export let show_label: boolean;
	export let show_download_button = true;
	export let show_share_button = false;
	export let i18n: I18nFormatter;
	export let height: number = 400;
</script>

<BlockLabel {show_label} Icon={Image} label={label || i18n("image.image")} />
{#if value === null || !value.url}
	<Empty unpadded_box={true} size="large"><Image /></Empty>
{:else}
	<div class="icon-buttons">
		{#if show_download_button}
			<a
				href={value.url}
				target={window.__is_colab__ ? "_blank" : null}
				download={"image"}
			>
				<IconButton Icon={Download} label={i18n("common.download")} />
			</a>
		{/if}
		{#if show_share_button}
			<ShareButton
				{i18n}
				on:share
				on:error
				formatter={async (value) => {
					if (!value) return "";
					let url = await uploadToHuggingFace(value, "base64");
					return `<img src="${url}" />`;
				}}
				{value}
			/>
		{/if}
	</div>
	<SveltePannellum div_id="pannellum-preview-{value.orig_name}" panorama={value.url} height={height}/>
{/if}

<style>
	.icon-buttons {
		display: flex;
		position: absolute;
		top: 6px;
		right: 6px;
		gap: var(--size-1);
	}
</style>
