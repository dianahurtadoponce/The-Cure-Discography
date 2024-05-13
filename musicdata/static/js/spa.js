function buildRow(key, value) {
    var tr = document.createElement("tr");
    var td = document.createElement("td");
    td.textContent = key+":";
    tr.appendChild(td);
    td = document.createElement("td");
    td.textContent = value;
    tr.appendChild(td);
    return(tr);
   }

function showSongData(id) {
    console.log("Retrieving Song: "+id);
    var request = new XMLHttpRequest();
    var url = "/api/song/"+id
    request.onreadystatechange = function(){
        if (this.readyState == 4 && (this.status >= 200 && this.status < 400)) {
            var data = JSON.parse(this.responseText);
            var dynamic_div = document.getElementById("dynamic_content");
            dynamic_div.innerHTML = '';
            var h1 = document.createElement("h1");
            h1.textContent = data.song_id;
            dynamic_div.appendChild(h1);

            var new_table = document.createElement("table");
            var th_row = document.createElement("tr");
            var th = document.createElement("th");
            th.textContent = "Key";
            th_row.appendChild(th);
            th = document.createElement("th");
            th.textContent = "Value";
            th_row.appendChild(th);
            new_table.appendChild(th_row);

            new_table.appendChild(buildRow("Album", data.album.album_name));
            new_table.appendChild(buildRow("Release Date", data.album.release));
            new_table.appendChild(buildRow("Cover", data.album.cover));
            new_table.appendChild(buildRow("Popularity", data.album.popularity));
            new_table.appendChild(buildRow("Name", data.spec.song_name));
            new_table.appendChild(buildRow("Duration", data.spec.duration));
            new_table.appendChild(buildRow("Danceability", data.spec.danceability));
            new_table.appendChild(buildRow("Energy", data.spec.energy));
            new_table.appendChild(buildRow("Key", data.spec.key));
            new_table.appendChild(buildRow("Loudness", data.spec.loudness));
            new_table.appendChild(buildRow("Mode", data.spec.mode));
            new_table.appendChild(buildRow("Speechiness", data.spec.speechiness));
            new_table.appendChild(buildRow("Acousticness", data.spec.acousticness));
            new_table.appendChild(buildRow("Instrumentalness", data.spec.instrumentalness));
            new_table.appendChild(buildRow("Liveness", data.spec.liveness));
            new_table.appendChild(buildRow("Valence", data.spec.valence));
            new_table.appendChild(buildRow("Tempo", data.spec.tempo));
            new_table.appendChild(buildRow("Time Signature", data.spec.time_signature));
            new_table.appendChild(buildRow("Track Popularity", data.track_popularity));

            dynamic_div.appendChild(new_table);

            var a = document.createElement("a");
            a.setAttribute('href', 'javascript:void(0);');
            a.setAttribute('onClick', 'updateSongData('+id+');');
            a.textContent = "UPDATE RECORD";
            dynamic_div.appendChild(a);
            dynamic_div.appendChild(document.createElement("br"));
            a = document.createElement("a");
            a.setAttribute('href', 'javascript:void(0);');
            a.setAttribute('onClick', 'deleteSongData('+id+');');
            a.textContent = "DELETE RECORD";
            dynamic_div.appendChild(a);
        }
        else if (this.status > 400 || (this.status > 0 && this.status < 200)) {
            console.log("Song Record Request Failed: "+id+" "+this.status);
        }
    };
    
    request.open("GET", url, true);
    request.send();
}

function writeSongMenu() {
    console.log("Retrieving Song List");
    var request = new XMLHttpRequest();
    var url = "/api/songs";
    request.onreadystatechange = function() {
    if (this.readyState == 4 && (this.status >= 200 &&
   this.status < 400)) {
    var data = JSON.parse(this.responseText);
    var song_table_div = document.getElementById("song_table");
    song_table_div.innerHTML = '';
    var new_table = document.createElement("table");
    var th_row = document.createElement("tr");
    var th = document.createElement("th");
    th.textContent = "Song ID";
    th_row.appendChild(th);
    new_table.appendChild(th_row);
    data.forEach(function(song){
        var a = document.createElement("a");
        a.setAttribute('href', 'javascript:void(0);');
        a.setAttribute('onClick', 'showSongData('+song.id+');');
        a.textContent = song.song_id;
        var td = document.createElement("td");
        var tr = document.createElement("tr");
        td.appendChild(a);
        tr.appendChild(td);
        new_table.appendChild(tr);
       });
    song_table_div.appendChild(new_table);

    console.log(data);
    }
    else if (this.status > 400 || (this.status > 0 &&
   this.status < 200)) {
    console.log("Song List Request Failed: "+this.status);
    }
    };
    request.open("GET", url, true);
    request.send();
}

function writeInitialContent() {
    console.log("Writing main content");
    var contentHTML = "<h2>Select key mode</h2>\n";
    contentHTML += "<a href=\"/keylist/major\">Major</a> OR <a href=\"/keylist/minor\">Minor</a>\n";
    contentHTML += "<h2>Show album's songs</h2>\n";
    contentHTML += "<a href=\"/list/Pornography\">Pornography</a><br><a href=\"/list/The Top\">The Top</a><br><a href=\"/list/Concert - The Cure Live\">Concert - The Cure Live</a><br><a href=\"/list/The Head On The Door\">The Head On The Door</a><br><a href=\"/list/Kiss Me Kiss Me Kiss Me\">Kiss Me Kiss Me Kiss Me</a><br><a href=\"/list/Disintegration (Deluxe Edition [Remastered])\">Disintegration (Deluxe Edition [Remastered])</a><br><a href=\"/list/Mixed Up (Remastered 2018/Deluxe Edition)\">Mixed Up (Remastered 2018/Deluxe Edition)</a><br><a href=\"/list/Wish\">Wish</a><br><a href=\"/list/Paris\">Paris</a><br><a href=\"/list/Show\">Show</a><br><a href=\"/list/Wild Mood Swings\">Wild Mood Swings</a><br><a href=\"/list/Bloodflowers\">Bloodflowers</a><br><a href=\"/list/The Cure\">The Cure</a><br><a href=\"/list/Hypnagogic States\">Hypnagogic States</a><br><a href=\"/list/4:13 Dream\">4:13 Dream</a><br><a href=\"/list/Bestival Live 2011\">Bestival Live 2011</a>\n";
    contentHTML += "<br />\n";
    contentHTML += "<h2>Create Album Entry</h2>\n";
    contentHTML += "<a href=\"/create_album/\">Add a Album Entry</a>\n";
    contentHTML += "<br />\n";
    contentHTML += "<h2>Create Song Specs Entry</h2>\n";
    contentHTML += "<a href=\"/create_spec/\">Add a Song Specs Entry</a>\n";
    contentHTML += "<br />\n";
    contentHTML += "<h2>Create Song Entry to Data Base</h2>\n";
    contentHTML += "<a href=\"/create_song/\">Add Song Entry</a>\n";
    contentHTML += "<br />\n";
    content_region = document.getElementById("dynamic_content");
    content_region.innerHTML = contentHTML;
}

function initialisePage() {
    console.log("Page Initialised");
    writeSongMenu();
    writeInitialContent();
}