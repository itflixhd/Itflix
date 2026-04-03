<?php
// MyCinema — Lista de Títulos
// Gerado em: 03/04/2026, 14:49:43
// Total: 0 títulos

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$lista = [

];

echo json_encode(['total' => count($lista), 'items' => $lista]);
?>