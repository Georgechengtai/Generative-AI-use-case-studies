---
title: "DeepSeek-OCR: Reading by Seeing"
---

# DeepSeek-OCR: Reading by Seeing

!!! note "Editor's Word: Field Test"
    I tested this model to classify over 500 candidate attachments (CVs, reference letters, and others). It ran locally on a laptop and successfully sorted the documents, though the setup was not "plug-and-play".

    I switched to Qwen3 models eventually, but that's based on my purpose. The task requires OCR + classification + analysis. Deepseek-OCR specialises in OCR matters, but ain't trained for downstream tasks. I am fortunate enough to have access to frontier models in my department server too.

## What is DeepSeek-OCR?

DeepSeek-OCR is a model designed to convert images of text into data. Unlike traditional OCR (Optical Character Recognition) which identifies letters one by one, DeepSeek-OCR uses **Contexts Optical Compression**.

It treats the page as an image and compresses it into "visual tokens". This allows an AI model to process the visual layout and text simultaneously, rather than just reading a string of plain text.

## Technical Reality: Why Use It?

For most users, basic tools like Tesseract are sufficient. However, DeepSeek-OCR has specific advantages for researchers or developers working with local models:

1.  **Local Execution:** It runs efficiently on consumer hardware. In our tests, it required less than **4GB of VRAM**.
2.  **Apple Silicon Support:** It works well with the **MLX VLM library**, meaning it runs natively on MacBook without needing a cloud server or heavy NVIDIA GPUs.
3.  **Visual Context:** Because it generates visual tokens, it preserves the spatial relationship of text. This is useful for documents where *position* matters, like forms or CVs with complex layouts.

!!! info "Comparison: PaddleOCR vs. DeepSeek-OCR"
    *   **PaddleOCR:** General-purpose. Multiple language supported. Considerably faster and lightweight too.
    *   **DeepSeek-OCR:** Newer and more experimental. less friendly to non-english input (even Chinese). Good for upstream tasks and finetuning.

## Practical Application

In our field test, I used it to sort a large batch of sample files (e.g. CV, cover letter, reference letters). The model, to a limited extent, could identify document types based on their visual structure (e.g., distinguishing a letterhead from a resume layout) without needing to read every single word.

!!! tip "For Developers"
    This is a tool for building *other* tools. If you are building a local document sorter or a private RAG (Retrieval-Augmented Generation) system on a laptop, this model is a lightweight alternative to paid APIs.
