[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Github Latest Pre-Release](https://img.shields.io/github/release/PresidioVantage/html-header-chunking?include_prereleases&label=pre-release&logo=github)](https://github.com/PresidioVantage/html-header-chunking/releases)
[![Github Latest Release](https://img.shields.io/github/release/PresidioVantage/html-header-chunking?logo=github)](https://github.com/PresidioVantage/html-header-chunking/releases)
[![Continuous Integration](https://github.com/PresidioVantage/DEV-html-header-chunking/actions/workflows/html_header_chunking_CI.yml/badge.svg)](https://github.com/PresidioVantage/DEV-html-header-chunking/actions)

# HTML Chunking with Headers
## Presidio Vantage Information Systems

A lightweight (SAX) HTML parse "chunked" into sequence of contiguous text segments, each with all "relevant" headers.
Chunks are always delimited by relevant headers, but also by a (configurable) set of tags between-which to chunk.
This is a "tree-capitator," if you will. 🪓🌳🔗

The API entry-point is in `src/html_header_chunking/chunker`.
The logical algorithm and data-structures are in `src/html_header_chunking/handler`.

Example usage:

	from html_header_chunking.chunker import get_chunker
	
	# default chunker is "lxml" for loose html
	with get_chunker() as chunker:
		
		# example of favorable structure yielding high-quality chunks
		# prints chunk-events directly
		chunker.parse_events(
			["https://plato.stanford.edu/entries/goedel/"],
			print)
		
		# example of moderate structure yielding medium-quality chunks
		# gets collection of chunks and loops through them
		q = chunker.parse_queue(
			["https://en.wikipedia.org/wiki/Kurt_G%C3%B6del"])
		while q:
			print(q.popleft())
		
		# examples of challenging structure yielding poor-quality chunks
		l = [
			"https://www.gutenberg.org/cache/epub/56852/pg56852-images.html",
			"https://www.cnn.com/2023/09/25/opinions/opinion-vincent-doumeizel-seaweed-scn-climate-c2e-spc-intl"]
		for c in chunker.parse_chunk_sequence(l):
			print(c)
	
	# example of mitigating/improving challenging structure by focusing only on html 'h4' and 'h5'
	with get_chunker("lxml", ["h4", "h5"]):
		chunker.parse_events(
			["https://www.gutenberg.org/cache/epub/56852/pg56852-images.html"],
			print)
	
	# example of using selenium on a page which requires javascript to load contents
	print("using default lxml produces very few chunks:")
	with get_chunker():
		chunker.parse_events(
			["https://www.youtube.com/watch?v=rfscVS0vtbw"],
			print)
	print("using selenium produces many more chunks:")
	with get_chunker("selenium"):
		chunker.parse_events(
			["https://www.youtube.com/watch?v=rfscVS0vtbw"],
			print)
