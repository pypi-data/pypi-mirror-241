from dataclasses import dataclass, field
from typing import Dict, List

from scfile.consts import MODEL_ROOT_BONE_ID, Normalization


def scaled(scale: float, i: float) -> float:
    return scale * i / Normalization.SCALING_FACTOR


@dataclass
class Vector:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


@dataclass
class Texture:
    u: float = 0.0
    v: float = 0.0


@dataclass
class VertexBone:
    ids: Dict[int, int] = field(default_factory=dict)
    weights: Dict[int, float] = field(default_factory=dict)


@dataclass
class Vertex:
    position: Vector = field(default_factory=Vector)
    normals: Vector = field(default_factory=Vector)
    texture: Texture = field(default_factory=Texture)
    bone: VertexBone = field(default_factory=VertexBone)
    weight: float = 0.0


@dataclass
class Polygon:
    vertex1: int = 0
    vertex2: int = 0
    vertex3: int = 0


@dataclass
class Mesh:
    name: bytes = b"name"
    material: bytes = b"material"
    link_count: int = 0
    vertices: List[Vertex] = field(default_factory=lambda: [Vertex()])
    polygons: List[Polygon] = field(default_factory=lambda: [Polygon()])

    def resize_vertices(self, count: int):
        self.vertices = [Vertex() for _ in range(count)]

    def resize_polygons(self, count: int):
        self.polygons = [Polygon() for _ in range(count)]


@dataclass
class Bone:
    name: bytes = b"bone"
    parent_id: int = MODEL_ROOT_BONE_ID
    position: Vector = field(default_factory=Vector)
    rotation: Vector = field(default_factory=Vector)


@dataclass
class Skeleton:
    bones: Dict[int, Bone] = field(default_factory=lambda: {0: Bone()})


@dataclass
class Model:
    meshes: Dict[int, Mesh] = field(default_factory=lambda: {0: Mesh()})
    skeleton: Skeleton = field(default_factory=Skeleton)
