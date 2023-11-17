<script lang="ts">
    export let div_id: string;
    export let panorama: string;
    export let height: number = 400;

    import { onMount } from 'svelte';
    import "pannellum";
    import 'pannellum/build/pannellum.css'

    onMount(() => {
        window.pannellum.viewer(
            div_id, {
            "type": "equirectangular",
            "panorama": panorama,
            });
        });
</script>

<!-- <div id="div-pannellum" alt={alt_text}></div> -->
<div id={div_id} style="height: {height}px;"></div>