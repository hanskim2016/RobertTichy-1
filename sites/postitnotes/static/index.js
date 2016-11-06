$(document).ready(function() {
  //
  //  Load Response Data from $.get() calls into the #notes div
  //  using html string built here.
  //
  function loadNotes(resp) {
    //   <div class='postit'>
    //     <div class='postittext'>
    //       <span class='h5 black'>:</span>
    //     </div>
    //     <div class='x_del'>X</div>
    // </div>
    var htmlStr = ""; // we create an empty string to clear out All the post it notes on display
    for(var i = 0; i < resp.notes.length; i++) {
      htmlStr += "<div id='"+resp.notes[i].id+"' class='postit'><div class='postittext'>";
      htmlStr += "<span class='h5 black'>" + resp.notes[i].subject +': ' +"</span>";
      if (resp.notes[i].note !== null) {
        htmlStr += resp.notes[i].note;
      }
      htmlStr += "</div><a class='x_del' data='notes/"+resp.notes[i].id+"/delete'>X</a></div>";
    }
    $('#notes').html(htmlStr);
  }
  //
  //  Ordinary load functions built without any search
  //  Criteria.  (load, page right, page left)
  //
  function ajaxLoad(arg) {
    if (!arg) {
      var path = '/notes';
    }
    else {
      path = '/notes/'+arg;
    }
    console.log("Get "+path);
    $.get(path, function(response) {
    loadNotes(response)}, 'json');;
  }
  //
  //  Main processing begins within
  //  $(document).ready()
  //
  console.log('JQuery loaded.');
  if (once !== true) {
    // console.log('initial load some notes')
    ajaxLoad();
    var once = true;
  }
  //
  //  Page Left
  //
  $('#left').click(function(){
    ajaxLoad('left');
  });
  //
  //  Page Right
  //
  $('#right').click(function(){
    ajaxLoad('right');
  });
  //
  // to use .on() we need to specify mouseenter() and mouseleave()
  // separately...
  //
  $('#notes').on('mouseenter','.postit',
    function(){
      // console.log('hovering in');
      //
      //  move Mouse into a post-it note and make
      //  "X" appear in upper right of note for delete action
      //
      $(this).find('a.x_del').show()
        $('a.x_del').on('click',function() {
          var link = $(this).attr('data');
          $.get(link,function(resp){
            ajaxLoad();
          });
        });
      //
      //  within a post-it note, clicking will open the note
      //  for editing.
      //
      $(this).click(function() {
        var id = $(this).attr('id');
        var path = 'notes/'+id+'/edit';
        $.get(path,{'id':id},
          function(result) {
            // replace note html with note input form html
            $("div#"+id).find('div.postittext').replaceWith(result);
            // take changes to form values and update table in DB
            $("div#"+id).find('.postitinput form').change(
              function(){$.post(path,$(this).serialize(),
                function(result) {
                  ajaxLoad();
                  return false;
                },'html');
              });
            return false;
          },'html'
        );
      });
    });
  //
  //  As mouse leaves a post-it note,
  //  remove the "X" so that deleting that note is not available
  //  and remove the .click handler for all X's
  //
  $('#notes').on('mouseleave','.postit',
    function(){
      // console.log('hovering out');
      $('a.x_del').off('click');
      $(this).find('a.x_del').hide();
    }
  );
  //
  //  User enters Note Subject at top and presses Create button
  //
  $('form.create').submit(function() {
    console.log('fake submit');
    // drive the note subject to the notes table in DB
    // and reload the note on screen so new note is available
    $.post('/notes/create', $(this).serialize(),function(row) {
      console.log("Row=",row);
      if (row >1) {
        $('#subject').val("");
        ajaxLoad();
      }
    })
    return false;
  });
  //
  //  Take search filter input and perform special load of notes
  //  that meet search criteria
  //
  $('form.search').submit(function() {
    console.log('search fake submit');
    var path = '/notes/'+$('#search').val()+'/search'
    console.log(path)
    $.get(path,function(data) {
      console.log("data=",data);
        loadNotes(data);
    });
    return false;
  });
})
