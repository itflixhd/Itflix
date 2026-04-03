<?php
// MyCinema — Lista de Títulos
// Gerado em: 03/04/2026, 14:50:54
// Total: 1 títulos

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$lista = [
  ['id'=>1775238654360,'name'=>'Devoradores de Estrelas','type'=>'movie','tmdbCode'=>'687163','poster'=>'https://image.tmdb.org/t/p/w342/bOzG3SG6gBxHGGHYiq7xXeNb1bG.jpg','magnetUrl'=>'magnet:?xt=urn:btih:A76458790115F4CE9F3288AF3808799C2ED483EB&dn=Project.Hail.Mary.2026.1080p.CAMRip.Dublado.Official.mkv&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce','year'=>'2026','rating'=>'8.2','addedAt'=>'03/04/2026','source'=>'local'],
];

echo json_encode(['total' => count($lista), 'items' => $lista]);
?>