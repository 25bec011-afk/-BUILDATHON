<!DOCTYPE html>
<html>
<head>
<title>FPS Game</title>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/examples/js/controls/PointerLockControls.js"></script>
<style>
body { margin:0; overflow:hidden; background:black; }
#start {
    position:absolute;
    top:40%;
    width:100%;
    text-align:center;
    color:white;
    font-size:20px;
    cursor:pointer;
}
</style>
</head>
<body>

<div id="start">CLICK TO START FPS</div>

<script>
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x202020);

const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// LIGHT
const light = new THREE.HemisphereLight(0xffffff, 0x444444);
scene.add(light);

// FLOOR
const floor = new THREE.Mesh(
    new THREE.PlaneGeometry(100,100),
    new THREE.MeshStandardMaterial({color:0x333333})
);
floor.rotation.x = -Math.PI/2;
scene.add(floor);

// CONTROLS
const controls = new THREE.PointerLockControls(camera, document.body);

document.getElementById("start").onclick = () => {
    controls.lock();
};

// MOVEMENT
let move = {w:false,s:false,a:false,d:false};

document.addEventListener("keydown", e=>{
    if(e.code==="KeyW") move.w=true;
    if(e.code==="KeyS") move.s=true;
    if(e.code==="KeyA") move.a=true;
    if(e.code==="KeyD") move.d=true;
});

document.addEventListener("keyup", e=>{
    if(e.code==="KeyW") move.w=false;
    if(e.code==="KeyS") move.s=false;
    if(e.code==="KeyA") move.a=false;
    if(e.code==="KeyD") move.d=false;
});

// ENEMIES
let enemies = [];

function createEnemy(){
    const e = new THREE.Mesh(
        new THREE.BoxGeometry(),
        new THREE.MeshStandardMaterial({color:0xff0000})
    );
    e.position.set(Math.random()*20-10,1,Math.random()*-20);
    scene.add(e);
    enemies.push(e);
}

for(let i=0;i<5;i++) createEnemy();

// SHOOT
const raycaster = new THREE.Raycaster();

document.addEventListener("click", ()=>{
    if(!controls.isLocked) return;

    raycaster.setFromCamera(new THREE.Vector2(0,0), camera);
    const hits = raycaster.intersectObjects(enemies);

    if(hits.length > 0){
        let hit = hits[0].object;
        scene.remove(hit);
        enemies = enemies.filter(e => e !== hit);
        createEnemy();
    }
});

// LOOP
function animate(){
    requestAnimationFrame(animate);

    let speed = 0.2;

    if(move.w) controls.moveForward(speed);
    if(move.s) controls.moveForward(-speed);
    if(move.a) controls.moveRight(-speed);
    if(move.d) controls.moveRight(speed);

    renderer.render(scene, camera);
}

animate();
</script>

</body>
</html>
