<script lang="ts">

    import type { FileData } from "@gradio/upload";
    import {normalise_file, blobToBase64} from "@gradio/upload";
    import { upload_files } from "@gradio/client";
    import { BaseButton } from "@gradio/button";

    import { tick, createEventDispatcher } from "svelte";

    export let button_label: string = "Upload";
    export let disabled = false;
    export let root: string;
    export let value: FileData[] = [];

    let hidden_upload: HTMLInputElement

    const dispatch = createEventDispatcher();

    export async function upload(
        file_data: FileData[],
        root: string,
        upload_fn: typeof upload_files | undefined = upload_files
    ): Promise<FileData[]> {
        let files = (Array.isArray(file_data) ? file_data : [file_data]).map(
            (file_data) => file_data.blob!
        );

        await upload_fn(root, files).then(async (response) => {
            if (response.error) {
                (Array.isArray(file_data) ? file_data : [file_data]).forEach(
                    async (file_data, i) => {
                        file_data.data = await blobToBase64(file_data.blob!);
                        file_data.blob = undefined;
                    }
                );
            } else {
                (Array.isArray(file_data) ? file_data : [file_data]).forEach((f, i) => {
                    if (response.files) {
                        f.orig_name = f.name;
                        f.name = response.files[i];
                        f.is_file = true;
                        f.blob = undefined;
                        normalise_file(f, root, null);
                    }
                });
            }
        });
        return file_data;
    }

    export async function prepare_files(files: File[]): Promise<FileData[]> {
        var all_file_data: FileData[] = [];
        files.forEach((f, i) => {
            all_file_data[i] = {
                name: f.name,
                size: f.size,
                data: "",
                blob: f
            };
        });
        return all_file_data;
    }

    async function loadFiles(files: FileList): Promise<void> {
		let _files: File[] = Array.from(files);
		if (!files.length) {
			return;
		}
		let all_file_data = await prepare_files(_files);
		await tick();
		all_file_data = await upload(all_file_data, root);
		dispatch("upload");
		value = all_file_data;
	}

	async function loadFilesFromUpload(e: Event): Promise<void> {
		const target = e.target as HTMLInputElement;

		if (!target.files) return;
		await loadFiles(target.files);
	}

    function openFileUpload(): void {
		hidden_upload.click();
	}

</script>

<input
    style="display: none;"
    accept={null}
    type="file"
    bind:this={hidden_upload}
    on:change={loadFilesFromUpload}
    multiple={true}
    on:click={loadFilesFromUpload}
/>

<BaseButton
    size={"lg"}
    variant={"secondary"}
    elem_id=""
    elem_classes={[]}
    visible={true}
    on:click={openFileUpload}
    scale={null}
    min-width={undefined}
    {disabled}
> 
    {button_label}
</BaseButton>



