var stepped = 0, chunks = 0, rows = 0;
var start, end;
var parser;
var pauseChecked = false;
var printStepChecked = false;

$(function()
{
	$('#submit-parse').click(function()
	{
		stepped = 0;
		chunks = 0;
		rows = 0;

		var txt = $('#input').val();
		var localChunkSize = $('#localChunkSize').val();
		var remoteChunkSize = $('#remoteChunkSize').val();
		var files = $('#files')[0].files;

		// NOTE: Chunk size does not get reset if changed and then set back to empty/default value
		if (localChunkSize)
			Papa.LocalChunkSize = localChunkSize;
		if (remoteChunkSize)
			Papa.RemoteChunkSize = remoteChunkSize;

		pauseChecked = $('#step-pause').prop('checked');
		printStepChecked = $('#print-steps').prop('checked');


		if (files.length > 0)
		{
				for (var i = 0; i < files.length; i++)
				{
					if (files[i].size > 1024 * 1024 * 10)
					{
						alert("A file you've selected is larger than 10 MB; please choose to stream or chunk the input to prevent the browser from crashing.");
						return;
					}
				}
			
			$('#files').parse({
				before: function(file, inputElem)
				{
					console.log("Archivo: ", file);
				},
				complete: function()
				{
					console.log("Se termino de cargar todos los archivos");
				}
			});
		}
		else
		{
			start = performance.now();
			var results = Papa.parse(txt, config);
			console.log("Synchronous parse results:", results);
		}
	});

});



