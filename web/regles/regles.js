// Affichage de l'image
$('img').click(function(){
	$('.all').fadeToggle();
	$('.all').find('img').attr('src', $(this).attr('src'));
});

// Disparition de l'image
$('.all').click(function(){
	$(this).fadeToggle();
})