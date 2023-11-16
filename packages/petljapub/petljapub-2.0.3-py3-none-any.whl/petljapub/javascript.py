from .messages import msg

# javascript support to switching languages in the HTML file
def add_switcher(md, langs, switcher_id=0):
    js_switches = "\n<ul class='language-switcher'>\n"
    for lang in langs:
        js_switches += "<li><a href='javascript:displaySolutionByLanguage(\"{}-{}\", {})'>{}</a></li>\n".format(lang, switcher_id, switcher_id, lang)
    js_switches += "</ul>\n\n"
    
    js_switcher = '''
        
<script type="text/javascript">
   function displaySolutionByLanguage(lang, switcher_id) {{
      var sol_divs = document.getElementsByClassName("sol");
      for (var i = 0; i < sol_divs.length; i++)
             if (sol_divs[i].id.endsWith(switcher_id.toString()))
                  sol_divs[i].style.display = "none";
      document.getElementById("sol-" + lang).style.display = "block";
   }}
   displaySolutionByLanguage(\"{}-{}\", {})
</script>

    '''.format(langs[0], switcher_id, switcher_id)
        
    return js_switches + md + js_switcher

def div(md, lang, switcher_id=0):
    return "<div id='sol-{}-{}' class='sol'>\n{}\n</div>\n".format(lang, switcher_id, md)

def abc_question(spec, question_id=0):
    options = []
    if "multiple" in spec and spec["multiple"]:
        button_type = "checkbox"
    else:
        button_type = "radio"
    
    for answer in spec["answers"]:
        options.append("<input type='{}' name='{}_abc_{}'></input> {}".format(button_type, button_type, question_id, answer))
    
    div = """
<div class='abc' id='abc_{}'>
   <p class='abc_question'>{}</p>
   <p class='abc_answers'>{}</p>
   <p class='abc_button'><input type='button' value='{}' /></p>
   <p class='abc_status'></p>
</div>

<script type="text/javascript">
    var div_abc_{} = document.getElementById('abc_{}');
    var button = div_abc_{}.getElementsByClassName("abc_button")[0];
    button.addEventListener("click", function() {{ 
        var p_answers = div_abc_{}.getElementsByClassName("abc_answers")[0];
        var p_status = div_abc_{}.getElementsByClassName("abc_status")[0];
        var buttons = p_answers.getElementsByTagName("input");
        var given_answers = [];
        for (var i = 0; i < buttons.length; i++)
            if (buttons[i].checked)
               given_answers.push(String.fromCharCode("a".charCodeAt(0) + i));
        if (JSON.stringify(given_answers).replace(/"/g, "'") == "{}")
            p_status.innerHTML = "OK";
        else 
            p_status.innerHTML = "NOT OK";
    }});
</script>
"""
    return div.format(question_id, spec["question"], "\n".join(options), msg("CHECK"), question_id, question_id, question_id, question_id, question_id, spec["correct"])


def iframe(file_name, title="", height=0, popup=False):
    if title == None:
        title = ""
    if height == None:
        height = 0
    scrolling = "" if not popup else " scrolling=\"no\""
    return "<iframe src='{}' title='{}' style='width: 100%; height: {}px' frameBorder='0'{}></iframe>".format(file_name, title, height, scrolling)

def popup(button, content, popup_id=0):
    code = """\n\n<button id='showPopup{}'>{}</button>

<div id='popup{}' class='popupbg'>
<div class='popupclose'>
<span id='closePopup{}'>✖</span>
</div>
<div class='popup'>
{}
</div>
</div>

<script>
document.getElementById('showPopup{}').addEventListener("click", function() {{
  document.getElementById("popup{}").style.visibility="visible";
}});
document.getElementById('closePopup{}').addEventListener("click", function() {{
 document.getElementById("popup{}").style.visibility="hidden";
}});
</script>"""
    
    return code.format(popup_id, button, popup_id, popup_id, content, popup_id, popup_id, popup_id, popup_id)

def resize_iframes(md):
    code = """

<script type="text/javascript">
// Function to resize a single iframe
function resizeIframe(iframe) {
     if (iframe && iframe.contentWindow && iframe.contentWindow.document.body) {
        const document = iframe.contentWindow.document;
        const totalHeight = Math.max(
             document.body.clientHeight,
             document.body.scrollHeight,
             document.body.offsetHeight,
             document.documentElement.clientHeight,
             document.documentElement.scrollHeight,
             document.documentElement.offsetHeight
        );
        iframe.style.height = `${totalHeight}px`;
        console.log(iframe, totalHeight);
     }
}

// Function to resize all iframes with the class "resize-iframe"
function resizeAllIframes() {
     const iframes = document.querySelectorAll('iframe');
     iframes.forEach((iframe) => {
         resizeIframe(iframe);
     });
}

// Call the resizeAllIframes function whenever the iframes' content is loaded or changes
window.addEventListener('load', resizeAllIframes);
</script>
"""
    
    return code + md;

