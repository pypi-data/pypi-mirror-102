---
title: JSON Schema for Humans
---

{% include README.md %}

# Configuration options
<iframe style="width: 100%; height: 60vh" src="assets/config_schema.html"></iframe>

# Configuration options (markdown format)
<div style="width: 100%; height: 60vh; overflow: auto;" markdown="1">

{% capture my_include %}{% include config_schema.md %}{% endcapture %}
{{ my_include  }}

</div>

# Examples
{% for example in site.data.examples %}
## {{ example.display_name }}

{{ example.description }}

<details><summary style="font-size:20px; cursor:pointer; text-decoration: underline">Click here to expand source JSON Schema...</summary>
<p>
{% highlight json %}
{% include examples/{{ example.name }}.json %}
{% endhighlight %}
</p>
</details>

<details><summary style="font-size:20px; cursor:pointer; text-decoration: underline">Click here to expand the rendered result using js template...</summary>
<p>
<iframe style="width: 100%; height: 60vh" src="assets/examples_js/{{ example.name }}.html"></iframe>
</p>
</details>

<details><summary style="font-size:20px; cursor:pointer; text-decoration: underline">Click here to expand the rendered result using flat template...</summary>
<p>
<iframe style="width: 100%; height: 60vh" src="assets/examples_flat/{{ example.name }}.html"></iframe>
</p>
</details>

<details><summary style="font-size:20px; cursor:pointer; text-decoration: underline">Click here to expand the rendered result using md template with badge option enabled...</summary>
<p>
<div style="width: 100%; height: 60vh; overflow: auto;" markdown="1">

{% capture my_include %}{% include examples_md_with_badge/{{ example.name }}.md %}{% endcapture %}
{{ my_include  }}

</div>
</p>
</details>
<br/>

{% endfor %}