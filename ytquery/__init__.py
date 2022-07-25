import re, urllib.request, urllib.parse

def find(search):
	query_string = urllib.parse.urlencode({
		"search_query": search
	})
	html_content = urllib.request.urlopen(
		"http://www.youtube.com/results?" + query_string
	)
	search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
	return "http://www.youtube.com/watch?v=" + search_results[0]