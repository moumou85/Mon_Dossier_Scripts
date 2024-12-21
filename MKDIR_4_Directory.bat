@echo off
:: Definir le chemin du projet
set "CheminProjet=D:\QA\Session 3\Language de Script\TP1"

:: Creer les dossiers
mkdir "%CheminProjet%\Requirement"
mkdir "%CheminProjet%\TestPlan"
mkdir "%CheminProjet%\TestCase"
mkdir "%CheminProjet%\TestReport"

echo Les dossiers ont bien ete cree dans %CheminProjet%
