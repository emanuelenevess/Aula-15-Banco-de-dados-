INSERT INTO tarefa (nomeTarefa, descricao, categoria, dataPrazo, prioridade, status)
VALUES
('Trabalho de História',
'Capítulo 4 e resumo de 2 páginas',
'Escola', '2026-12-10', 'ALTA', 'Pendente'),
('Trabalho de Portugues', 'Verbos no passado', 'Escola','2026-11-26', 'MEDIA', 'Pendente'),
('Reunião de alinhamento', 'Apresentar resultados semanais para a equipe', 'Trabalho', '2026-11-16', 'ALTA', 'Pendente'), 
('Consulta no dentista', 'Limpeza e avaliação de rotina', 'Saúde', '2026-11-24', 'MEDIA', 'Pendente'), 
('Comprar ração do cachorro', 'Pacote de 15kg sabor frango', 'Casa', '2026-11-15', 'ALTA', 'Pendente'), 
('Estudar SQL', 'Praticar comandos JOIN e GROUP BY', 'Estudos', '2026-11-30', 'MEDIA', 'Em Andamento'), 
('Fazer revisão do carro', 'Troca de óleo e alinhamento', 'Pessoal', '2026-12-12', 'BAIXA', 'Pendente');

SELECT * FROM tarefa;