<svelte:options accessors={true} />

<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { BlockTitle } from "@gradio/atoms";
	import { Block } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import type {FileData} from "@gradio/upload";
	import { tick } from "svelte";
	import Button from "./Button.svelte";

	export let gradio: Gradio<{
		text_change: never;
		text_submit: never;
		file_upload: never;
		file_change: never;
	}>;

	export let label = "Textbox With Attachments";
	export let button_label
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: {text: string, attachments: FileData[]} | null = {text: "", attachments: []};
	export let placeholder = "";
	export let show_label: boolean;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus | undefined = undefined;
	export let root: string; 

	export let mode: "static" | "interactive";
	export let rtl = false;

	let el: HTMLTextAreaElement | HTMLInputElement;
	const container = true;

	async function handle_keypress(e: KeyboardEvent): Promise<void> {
		await tick();
		if (e.key === "Enter") {
			e.preventDefault();
			gradio.dispatch("text_submit");
		}
	}

	$: if (value === null) value = {text: "", attachments: []};
	
	$: text_change = value.text;
	$: text_change, gradio.dispatch("text_change");
</script>

<Block
	{visible}
	{elem_id}
	{elem_classes}
	{scale}
	{min_width}
	allow_overflow={false}
	padding={true}
>
	{#if loading_status}
		<StatusTracker
			autoscroll={gradio.autoscroll}
			i18n={gradio.i18n}
			{...loading_status}
		/>
	{/if}

	<BlockTitle {show_label} info={undefined}>{label}</BlockTitle>
	<div class="flex-row">
		<div class="parent-input">
			<label class:container>
					<input
					data-testid="textbox"
					type="text"
					class="scroll-hide"
					bind:value={value.text}
					bind:this={el}
					{placeholder}
					disabled={mode === "static"}
					dir={rtl ? "rtl" : "ltr"}
					on:keypress={handle_keypress}
					on:change={() => gradio.dispatch("text_change")}
					/>
			</label>
		</div>
		<div class="upload-btn">
			<Button
				bind:value={value.attachments}
				{root}
				disabled={mode === "static"}
				{button_label}
				on:upload={() => gradio.dispatch("file_upload")}
			/>
		</div>
	</div>

</Block>

<style>
	label {
		display: block;
		width: 100%;
	}

	.flex-row {
		display: flex;
		flex-direction: row;
		width: 100%;
	}

	.upload-btn {
		display: inline-flex;
		position: relative;
		width: 5%;
	}

	.parent-input {
		width: 93%;
		padding-right: 2%;
	}

	input {
		display: flex;
		position: relative;
		outline: none !important;
		box-shadow: var(--input-shadow);
		background: var(--input-background-fill);
		padding: var(--input-padding);
		width: 100%;
		color: var(--body-text-color);
		font-weight: var(--input-text-weight);
		font-size: var(--input-text-size);
		line-height: var(--line-sm);
		border: none;
	}
	.container > input {
		border: var(--input-border-width) solid var(--input-border-color);
		border-radius: var(--input-radius);
	}
	input:disabled {
		-webkit-text-fill-color: var(--body-text-color);
		-webkit-opacity: 1;
		opacity: 1;
	}

	input:focus {
		box-shadow: var(--input-shadow-focus);
		border-color: var(--input-border-color-focus);
	}

	input::placeholder {
		color: var(--input-placeholder-color);
	}
</style>
